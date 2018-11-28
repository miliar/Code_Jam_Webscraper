#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int inf = 0x3f3f3f3f;
const double eps = 1e-8;
const int maxn = 1e4+10;
int DP[1010][1010];
int a[1010];
int f(int x)
{
    return x/2 + x%2;
}
int main()
{
    freopen("B-large.in", "r",stdin);
    freopen("B-large.out", "w",stdout);
    int t;
    int cas=1;
    int n;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        memset(DP,0x3f,sizeof(DP));
        for(int i=1; i<=n; i++)
        {
            scanf("%d",a+i);
        }
        memset(DP[0],0,sizeof(DP[0]));
        for(int i=1; i<=n; i++)
        {
            for(int j=1; j<=1000; j++)
            {
                DP[i][j] = DP[i][j-1];
                DP[i][j] = min(DP[i][j], DP[i-1][j]+(a[i]-1)/j);
            }
        }
        int ans = 10000000;
        for(int j=0; j <= 1000; j++)
        {
            ans=min(ans, DP[n][j]+j);
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
