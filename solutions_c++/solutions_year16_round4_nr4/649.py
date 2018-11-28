#define N (1<<8)
#include <bits/stdc++.h>

using namespace std;

int T,n,k,cas;
double p[N],dp[N][N],v[N];

int calc(int x)
{
    int cnt=0;
    for(;x;x>>=1) cnt+=x&1;
    return cnt;
}

double solve()
{
    dp[0][0]=1;
    for(int i=1;i<=k;i++)
        for(int j=0;j<=i;j++)
        {
            dp[i][j]=dp[i-1][j]*(1.-v[i]);
            if(j>0) dp[i][j]+=dp[i-1][j-1]*v[i];
        }
    return dp[k][k/2];
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    for(cin>>T;T--;)
    {
        cin>>n>>k;
        for(int i=0;i<n;i++)
            scanf("%lf",p+i);
        sort(p,p+n);

        double res=0;
        for(int i=0;i<k;i++)
        {
            int cnt=1;
            for(int j=0;j<i;j++)
                v[cnt++]=p[j];
            for(int j=n-1;j>=n-(k-i);j--)
                v[cnt++]=p[j];
            res=max(res,solve());
        }
        printf("Case #%d: %.9f\n",++cas,res);
    }
    return 0;
}
