#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<time.h>
#include<cmath>
#include<vector>
#include <iomanip>
#define PB(u)  push_back(u);
#define AA   first
#define BB   second
#define inf 0x3f3f3f3f
using namespace std ;
#define MAX 30
#define sz size()
typedef long long ll ;
typedef pair<int,int> PII ;
const double eps=1e-8;
const double pi=acos(-1.0);

double dp[MAX][MAX];
int a[MAX];
double p[MAX];

int main()
{
    //freopen("intput.in","r",stdin);
    //freopen("output.out","w",stdout);
    int T,cas=1;
    cin>>T;
    while(T--)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=1;i<=n;i++) scanf("%lf",&p[i]);
        double ans=0;
        for(int i=0;i<(1<<n);i++)
        {
            if(__builtin_popcount(i)!=m) continue ;
            int cnt=1;
            for(int j=0;j<n;j++)
            {
                if((i>>j)&1)
                    a[cnt++]=j;
            }
            memset(dp,0,sizeof(dp));
            dp[0][0]=1;
            for(int k=1;k<=m;k++)
            {
                int id=a[k];
                cout<<id<<endl ;
                for(int j=0;j<=min(k,m/2);j++)
                {
                    dp[k][j]=dp[k-1][j]*(1-p[id]);
                    if(j>=1)
                        dp[k][j]+=dp[k-1][j-1]*p[id];
                }
            }
            ans=max(ans,dp[m][m/2]);
        }
        printf("Case #%d: %.10f\n",cas++,dp[m][m/2]);
    }
    return 0 ;
}
