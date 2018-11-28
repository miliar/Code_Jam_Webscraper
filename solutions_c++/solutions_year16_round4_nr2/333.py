#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<queue>
using namespace std;

double p[207];
double dp[207][207];
double g[207];
main()
{
    freopen("b-large.in","r",stdin);
    freopen("b-large.out","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        int n,K;scanf("%d%d",&n,&K);
        for(int i=0;i<n;i++) scanf("%lf",&p[i]);
        sort(p,p+n);
        double ans=0;
        for(int i=0;i<n;i++)
        {
            for(int j=1;j<=K;j++)
            {
                g[j]=p[(i+j-1)%n];
            }
            for(int x=0;x<=K+2;x++)
            for(int y=0;y<=K+2;y++)
            dp[x][y]=0;
            dp[0][0]=1;
            for(int x=1;x<=K;x++)
            {
                dp[x][0]=dp[x-1][0]*(1-g[x]);
                for(int y=1;y<=x;y++)
                dp[x][y]=dp[x-1][y-1]*g[x]+dp[x-1][y]*(1-g[x]);
            }
            ans=max(ans,dp[K][K/2]);

        }
        printf("Case #%d: %.8f\n",++cas,ans);

    }
}
