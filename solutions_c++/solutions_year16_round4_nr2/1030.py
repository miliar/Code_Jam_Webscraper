#include <bits/stdc++.h>
using namespace std;
const int maxn=210;
double dp[maxn][maxn];
double ar[maxn],ans;
int n,k;
int peo[maxn];
double judge()
{
    dp[0][0]=1;
    for(int i=1;i<=k;i++)
    {
        double tmp=ar[peo[i]];
        for(int j=0;j<=i;j++)
        {
            if(j)
                dp[i][j]=tmp*dp[i-1][j-1]+(1-tmp)*dp[i-1][j];
            else
                dp[i][j]=(1-tmp)*dp[i-1][j];
        }
    }
    return dp[k][k/2];
}
void dfs(int cur,int tot)
{
    if(tot==k)
    {
        ans=max(ans,judge());
        return;
    }
    if(cur>n)  return;
    dfs(cur+1,tot);
    peo[tot+1]=cur;
    dfs(cur+1,tot+1);
}
void solve()
{
    scanf("%d%d",&n,&k);
    for(int i=1;i<=n;i++)
        scanf("%lf",&ar[i]);
    ans=0;
    dfs(1,0);
    printf("%lf\n",ans);
}
int main()
{
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
