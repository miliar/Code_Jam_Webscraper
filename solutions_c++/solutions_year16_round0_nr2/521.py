// B CZM1.0
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<algorithm>
using namespace std;

#define oo 0x3f3f3f3f
#define eps 1e-8
#define PI acos(-1.0)
const static int maxN = 1000;
typedef __int64 INT64;
typedef INT64 LL;

//#pragma comment(linker, "/STACK:1024000000,1024000000")

//#define __DEBUG__
#ifdef __DEBUG__
//#define _DP(fmt, arg...) printf("[%s %s %d] " fmt, __FILE__, __FUNCTION__, __LINE__, ##arg)
#define _DP(fmt, arg...) printf("[%d] " fmt, __LINE__, ##arg)
#else
#define _DP(fmt, arg...)
#endif

char s[10000];
int dp[105][105][2][3]; // 区间，正负，左右不翻 

int DP(int n)
{
    memset(dp, 0x3f, sizeof(dp));
    _DP("aaa\n");
    for (int i = 0; i < n; i++)
    {
        dp[i][i][0][0] = dp[i][i][0][1] = (s[i] != '+');
        dp[i][i][1][0] = dp[i][i][1][1] = (s[i] != '-');
        dp[i][i][0][2] = (s[i] == '+' ? 0 : oo);
        dp[i][i][1][2] = (s[i] == '-' ? 0 : oo);
    }
    _DP("aaa\n");
    for (int b = 1; b < n; b++)
    {
        for (int i = 0; i < n - b + 1; i++)
        {
            // dp[i][i+b]
            for (int j = i; j < i + b; j++)
            {
                for (int d = 0; d < 2; d++)
                {
                    _DP("b[%d], i[%d], d[%d]\n", b, i, d);
                    // 左翻 
                    dp[i][i+b][d][0] = min(dp[i][i+b][d][0], dp[i][j][d][0] + dp[j+1][i+b][d][2]);
                    dp[i][i+b][d][0] = min(dp[i][i+b][d][0], dp[i][j][d^1][0] + dp[j+1][i+b][d^1][1] + 1);
                    // 右翻 
                    dp[i][i+b][d][1] = min(dp[i][i+b][d][1], dp[i][j][d][2] + dp[j+1][i+b][d][1]);
                    dp[i][i+b][d][1] = min(dp[i][i+b][d][1], dp[i][j][d^1][0] + dp[j+1][i+b][d^1][1] + 1);
                    // 不翻
                    dp[i][i+b][d][2] = min(dp[i][i+b][d][2], dp[i][j][d][2] + dp[j+1][i+b][d][2]);
                }
            }
        }
    }
    return dp[0][n-1][0][0];
}

int main()
{
    int T;
    int cas = 1;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%s", s);
        printf("Case #%d: %d\n", cas++, DP(strlen(s)));
    }
    return 0;
}
