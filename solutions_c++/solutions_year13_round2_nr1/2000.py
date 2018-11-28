#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
#define maxn 4005

int n;
int a[maxn];
int dp[maxn][maxn];

int main()
{
    scanf("%d",&n);
    for (int i=1;i<=n;i++)
        scanf("%d",&a[i]);
    int ans=1;  
    for (int i=1;i<=n;i++)
    {
        int t=0;
        for (int j=0;j<i;j++)
        {
            dp[i][j]=dp[j][t]+1;
            if (a[i]==a[j]) t=j;
            ans=max(ans,dp[i][j]);
        }
    }
    printf("%d\n",ans);
    return 0;
}
