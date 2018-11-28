#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;
int dp[105][105],c[105],r[105];
int n,m;
int main()
{

    //freopen("B-large.in","r",stdin);
    //freopen("a.txt","r",stdin);
   //freopen("b.txt","w",stdout);
    int T,cc=1;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d",&n,&m);
        printf("Case #%d: ",cc++);
        memset(c,0,sizeof(c));
        memset(r,0,sizeof(r));
        for(int i=1;i<=n;++i)
        for(int j=1;j<=m;++j){
        scanf("%d",&dp[i][j]);
            c[j]=max(c[j],dp[i][j]);
            r[i]=max(r[i],dp[i][j]);
        }
        bool flg=1;
        for(int i=1;i<=n;++i){
            for(int j=1;j<=m;++j)
            if(dp[i][j]<r[i]&&dp[i][j]<c[j]){
                flg=0;
                break;
            }
            if(flg==0)break;
        }
        if(flg)printf("YES\n");
        else printf("NO\n");

    }
   return 0;
}
