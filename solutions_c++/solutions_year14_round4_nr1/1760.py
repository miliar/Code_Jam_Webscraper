#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>

using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int n;
    fin>>n;
    for(int t=1;t<=n;t++){
        int ans=0;
        int T,X;
        fin>>T>>X;
        cout<<X<<endl;
        int S[T];
        bool s[T];
        for(int i=0;i<T;i++){
            fin>>S[i];
            s[i]=false;
        }
        sort(S,S+T);
        for(int i=0;i<T;i++){
            //cout<<S[i]<<' ';
        }
        //cout<<endl;
        int lj=0;
        for(int i=T-1;i>0;i--){
            for(int j=0;S[i]+S[j]<=X&&j<i;j++){
                if(s[j]==false)lj=j;
            }
            if(s[i]==false&&s[lj]==false&&S[i]+S[lj]<=X&&lj<i){
                s[i]=true;
                s[lj]=true;
                ans++;
            }
        }
        //cout<<"ANS "<<ans<<endl;
        int ed=0;
        for(int i=0;i<T;i++){
            if(s[i]==true)continue;
            //cout<<S[i]<<' ';
            //cout<<S[i]<<' '<<ed<<endl;
            if(ed==0){
                ed=S[i];
            }
            else{
                if(ed+S[i]<=X){
                    ed=0;
                    ans++;
                }
                else{
                    ed=S[i];
                    ans++;
                }
            }
        }
        //cout<<endl;
        if(ed!=0)ans++;
        char ansstr[500];
        sprintf(ansstr,"Case #%d: %d\n",t,ans);
        fout<<ansstr;
        //cout<<ansstr;
    }
    return 0;
}
