#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define FI first
#define SE second
using namespace std;
typedef long long ll;
#define maxn 1000
double p[maxn];
double dp[205][500];
double tp[maxn];
int main()
{
    freopen("B-large (2).in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        for(int i=0;i<n;i++) scanf("%lf",p+i);
        sort(p,p+n);
        double ans=0;
        memset(dp,0,sizeof(dp));
        for(int i=0;i<=k;i++)
        {
            int tot=0;
            for(int j=0;j<i;j++) tp[tot++]=p[j];
            for(int j=n-1;j>n-k+i-1;j--) tp[tot++]=p[j];
            for(int j=0;j<430;j++) dp[0][j]=0;
            dp[0][0+200]=1.0;
            for(int j=0;j<k;j++)
            {
                for(int ppp=-k;ppp<k;ppp++)
                {
                    dp[j+1][ppp+200]=dp[j][ppp-1+200]*tp[j]+dp[j][ppp+1+200]*(1.0-tp[j]);
                }
            }
            ans=max(dp[k][200],ans);
        }
        printf("Case #%d: %.10f\n",cas,ans);
    }
}
