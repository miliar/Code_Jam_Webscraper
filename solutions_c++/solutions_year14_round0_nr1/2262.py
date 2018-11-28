#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int T,r1,r2;
int mat[2][5][5];
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.txt","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;++cas){
            cin>>r1;
            for(int i=1;i<=4;++i)
                    for(int j=1;j<=4;++j)
                            cin>>mat[0][i][j];
            cin>>r2;
            for(int i=1;i<=4;++i)
                    for(int j=1;j<=4;++j)
                            cin>>mat[1][i][j];
            int ans=-1;
            for(int j=1;j<=4;++j){
                    for(int k=1;k<=4;++k){
                            if(mat[1][r2][j]==mat[0][r1][k]){
                                if(ans==-1)
                                           ans=mat[0][r1][k];
                                else if(ans>0){
                                     ans=100;
                                }
                            }
                    }
            }
            printf("Case #%d: ",cas);
            if(ans<0){
                      puts("Volunteer cheated!");
            }
            else if(ans<=16)
                 printf("%d\n",ans);
            else puts("Bad magician!");
    }
    return 0;
}
