#include <cstdio>
#include <iostream>
using namespace std;

int mat[4][4];
void solve(){
     int x;
     int memo[17];
     scanf("%d",&x);
     for (int i=0;i<4;++i){
         for (int j=0;j<4;++j)
             scanf("%d",&mat[i][j]);
     }
     for (int i=0;i<17;++i) memo[i]=0;
     for (int i=0;i<4;++i) memo[mat[x-1][i]]+=1;
     scanf("%d",&x);
     for (int i=0;i<4;++i){
         for (int j=0;j<4;++j)
             scanf("%d",&mat[i][j]);
     }
     for (int i=0;i<4;++i) memo[mat[x-1][i]]+=1;
     
     int ans=0,ctr=0;
     for (int i=1;i<=16;++i){
         if (memo[i]==2){
            ans=i;
            ctr++;
         }
     }
     if (ctr==1) printf("%d\n",ans);
     if (ctr>1) printf("Bad magician!\n");
     if (ctr<1) printf("Volunteer cheated!\n");
}
int main(){
    int ntest;
    scanf("%d",&ntest);
    for (int test=1;test<=ntest;++test){
        printf("Case #%d: ",test);
        solve();
    }
    return 0;
}
