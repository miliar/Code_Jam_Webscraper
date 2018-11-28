#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <queue>

using namespace std;

typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

#define LL long long
#define ULL unsigned long long
#define m_p make_pair
#define l_b lower_bound
#define p_b push_back
#define w1 first
#define w2 second
#define maxlongint 2147483647
#define biglongint 2139062143

int TT,N,o,ans,a[1005],dp[1005][1005];

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);

    scanf("%d",&TT);
    for (int gb=1;gb<=TT;gb++)
    {
        scanf("%d",&N);
        for (int i=1;i<=N;i++) scanf("%d",&a[i]);
        memset(dp,127,sizeof(dp));
        dp[0][0]=0;
        for (int i=0;i<N;i++)
            for (int j=0;j<=1000;j++)
                if (dp[i][j]!=biglongint)
                    for (int k=0;k<=1000-j;k++)
                        dp[i+1][j+k]=min(dp[i+1][j+k],max(dp[i][j],(a[i+1]-1)/(k+1)+1));
        ans=maxlongint;
        for (int i=0;i<=1000;i++) ans=min(ans,dp[N][i]+i);
        printf("Case #%d: %d\n",gb,ans);
    }
    return 0;
}
