// A CZM1.0
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

#define oo 1000000000
#define eps 1e-8
#define PI acos(-1.0)
const static int maxN = 10000;
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

char s[maxN];
char t[maxN];

int dp[maxN][2];
int dpp[maxN][2];
int pos = 0;

void DFS(int i, int idx)
{
    if (i == 0)
    {
        t[pos] = s[i];
        return;
    }
    DFS(i - 1, dpp[i][idx]);
    if (idx)
    {
        pos--;
        t[pos] = s[i];
    }
    else
    {
        t[pos+i] = s[i];
    }
}

void DP()
{
    int len = strlen(s);
    memset(dp, 0, sizeof(dp));
    memset(dpp, -1, sizeof(dpp));
    dp[0][0] = dp[0][1] = s[0];
    for (int i = 1; i < len; i++)
    {
        dpp[i][0] = dpp[i][1] = dp[i-1][1] >= dp[i-1][0];
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]);
        dp[i][1] = s[i];
        _DP("%d %c %c %d %d\n", i, dp[i][0], dp[i][1], dpp[i][0], dpp[i][1]);
    }
    pos = len;
    DFS(len - 1, dp[len-1][1] >= dp[len-1][0]);
    t[pos + len] = 0;
}

int main()
{
    int T;
    int cas = 1;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%s", s);
        DP();
        printf("Case #%d: %s\n", cas++, t + pos);
    }
    return 0;
}
