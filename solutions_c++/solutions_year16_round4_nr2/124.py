#include<bits/stdc++.h>
using namespace std;


double p[205],b[205];
double dp[205][205];
double solv(int n)
{
    memset(dp,0,sizeof(dp));
    dp[0][0]=1.0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<=i;j++)
        {
            dp[j+1][i-j]+=dp[j][i-j]*b[i];
            dp[j][i-j+1]+=dp[j][i-j]*(1.0-b[i]);
        }
    }
    return dp[n/2][n/2];
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("2.txt","w",stdout);
    int t,ti=1;scanf("%d",&t);
    while(t--)
    {
        int n,k;scanf("%d%d",&n,&k);
        for(int i=0;i<n;i++)
            scanf("%lf",p+i);
        sort(p,p+n);
        double ans=0.0;
        for(int i=0;i<=k;i++)
        {
            int f=0;
            for(int z=0;z<i;z++)
                b[f++]=p[z];
            for(int z=i;z<k;z++)
                b[f++]=p[n-z+i-1];
            ans=max(ans,solv(k));
        }
        printf("Case #%d: %.8f\n",ti++,ans);
    }
    return 0;
}
