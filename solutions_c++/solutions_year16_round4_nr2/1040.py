#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
using namespace std;

double pro[233],p[233],dp[233][111],ans;
int n,K;

void dfs(int x,int y)
{
    if (y==K)
    {
        dp[0][0]=1;
        for (int i=1;i<=K;++i)
        {
            for (int j=0;j<=i;++j)
            {
                dp[i][j]=dp[i-1][j]*(1-p[i])+(j>0?dp[i-1][j-1]*p[i]:0);
            }
        }
        ans=max(ans,dp[K][K/2]);
        return;
    }
    if (x>n) return;
    if (n+1-x<K-y) return;
    dfs(x+1,y);
    p[y+1]=pro[x];
    dfs(x+1,y+1);
}

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        scanf("%d%d",&n,&K);
        for (int i=1;i<=n;++i) scanf("%lf",pro+i);
        printf("Case #%d: ",cas);
//        sort(pro+1,pro+n+1);
//        for (int i=1;i<=K/2;++i) p[i]=pro[i];
//        for (int i=n;i>n-K/2;--i) p[K/2+1+n-i]=pro[i];
        ans=0;
        dfs(1,0);
        printf("%.12f\n",ans);
    }
    return 0;
}
