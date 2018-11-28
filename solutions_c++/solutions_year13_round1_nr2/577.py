#include <stdio.h>
#include <string.h>
#include <algorithm>
#define MAX 13

using namespace std;

bool vis[MAX][MAX];
int dp[MAX][MAX],e,r,n,inp[MAX];

void solve(int x,int rem)
{
    int i;
    if (vis[x][rem]) return ;
    vis[x][rem]=1;
    dp[x][rem]=0;
    if (x==n) return ;
    for (i=0;i<=rem;i++)
    {
        solve(x+1,min(rem-i+r,e));
        dp[x][rem]=max(dp[x][rem],i*inp[x]+dp[x+1][min(rem-i+r,e)]);
    }
}

int main()
{
    freopen("bin.txt","r",stdin);
    freopen("bout.txt","w",stdout);
    int test,cas,i;
    scanf("%d",&test);
    for (cas=1;cas<=test;cas++)
    {
        scanf("%d%d%d",&e,&r,&n);
        for (i=0;i<n;i++) scanf("%d",&inp[i]);
        memset(vis,0,sizeof(vis));
        solve(0,e);
        printf("Case #%d: %d\n",cas,dp[0][e]);
    }
    return 0;
}
