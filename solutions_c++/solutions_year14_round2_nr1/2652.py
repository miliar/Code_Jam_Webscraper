#include<iostream>
#include<string>
#include<cmath>

using namespace std;
main()
{
    int T;cin>>T;
    for(int i=0;i<T;i++){
        int N;cin>>N;
        int j,cc[110],k;
        string s[110];
        char ch[110][110];
        int cm[110][110];
        string::iterator it;
        for(j=0;j<N;j++){
            cin>>s[j];cc[j]=0;cm[j][0]=0;
            for(it=s[j].begin(); it!=s[j].end();it++){
                ch[j][cc[j]]=*it;cm[j][cc[j]]++;
                if(*(it+1)!=*it) {cc[j]++;cm[j][cc[j]]=0;}
            }
        }
        int mm=0;
        for(j=0;j<N-1;j++){
            //cout<<cc[j];
            if(cc[j+1]!=cc[j]) {mm=1;break;}
        }
        if(mm==1){
            cout<<"Case #"<<i+1<<": Fegla Won"<<endl;continue;
        }
        int x=cc[0];
        for(j=0;j<N-1;j++){
            for(k=0;k<x;k++){
                if(ch[j+1][k]!=ch[j][k]) {mm=1;break;}
            }
            if(mm==1) break;
        }
        if(mm==1){
            cout<<"Case #"<<i+1<<": Fegla Won"<<endl;continue;
        }
        /*for(j=0;j<N;j++){
            for(k=0;k<x;k++)
                cout<<cm[j][k];
        }*/
        int mn[101];
        for(k=0;k<x;k++){
            mn[k]=0;
            for(j=0;j<N;j++){
                mn[k]+=cm[j][k];
            }
            mn[k]/=N;
            //cout<<mn[k];
        }
        int yy=0;
        for(k=0;k<x;k++){
            for(j=0;j<N;j++){
                yy+=abs(mn[k]-cm[j][k]);
            }
        }
        cout<<"Case #"<<i+1<<": "<<yy<<endl;
    }
}
