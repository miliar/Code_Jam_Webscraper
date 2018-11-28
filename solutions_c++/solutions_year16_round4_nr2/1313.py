#include<cstdio>
#include<cmath>
#include<stdlib.h>
#include<map>
#include<set>
#include<time.h>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define eps 1e-8
double dp[22][22][22];
int n,k;
double p[202];
int gettwo(int x)
{
    int ans=0;
    while(x)
    {
        ans+=x%2;
        x/=2;
    }
    return ans;
}
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    FILE *fp=fopen("B-small.out","w");
//    freopen("B-small-attempt0.out","w",stdout);
//    freopen("B-large-practice.in","r",stdin);
//    freopen("B-large-practice.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1; cas<=T; cas++)
    {
        printf("%d\n",cas);
        scanf("%d%d",&n,&k);
        for(int i=1;i<=n;i++)
            scanf("%lf",&p[i]);
        double ans=0.0;
        for(int i=0;i<(1<<n);i++)
        {
            vector<int>vec;
            if(gettwo(i)!=k)
                continue;
            for(int j=0;j<n;j++)
            {
                if(i&(1<<j))
                    vec.push_back(j);
            }
            memset(dp,0,sizeof(dp));
            dp[0][0][0]=1;
            for(int i=1;i<=k;i++)
            {
                for(int j=0;j<=k;j++)
                {
                    for(int t=0;t<=j;t++)
                    {
                        dp[i][j][t]+=dp[i-1][j][k];
                        if(j)
                        {
                            dp[i][j][t]+=dp[i-1][j-1][t-1]*p[vec[i-1]+1];
                            dp[i][j][t]+=dp[i-1][j-1][t]*(1-p[vec[i-1]+1]);
                        }
                    }
                }
            }
            ans=max(ans,dp[k][k][k/2]);
        }
        fprintf(fp,"Case #%d: %f\n",cas,ans);
    }
    return 0;
}
