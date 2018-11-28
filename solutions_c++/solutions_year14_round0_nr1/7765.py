#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;
ofstream fout("PA.out");
ifstream fin("PA.in");
int T,M[4][4];
int used[17];
int main()
{
    fin>>T;
    int a,b;
    for(int t=1;t<=T;t++){
        fill(used,used+17,0);
        fin>>a;
        for(int i=0;i<4;i++)
        for(int k=0;k<4;k++){
            fin>>M[i][k];
        }
        for(int k=0;k<4;k++){
            used[M[a-1][k]]+=1;
        }

        fin>>b;
        for(int i=0;i<4;i++)
        for(int k=0;k<4;k++){
            fin>>M[i][k];
        }
        for(int k=0;k<4;k++){
            used[M[b-1][k]]+=1;
        }

        int cnt=0,ans;
        for(int i=1;i<=16;i++){
            if(used[i]==2){
                ans=i;
                cnt++;
            }
        }

        fout<<"Case #"<<t<<": ";
        if(cnt==0){
            fout<<"Volunteer cheated!\n";
        }
        if(cnt==1){
            fout<<ans<<endl;;
        }
        if(cnt>1){
            fout<<"Bad magician!\n";
        }
    }
}

