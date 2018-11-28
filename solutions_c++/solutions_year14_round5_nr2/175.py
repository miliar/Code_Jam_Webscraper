#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
using namespace std;


typedef long long LL;
#define INF 0x3f3f3f3f
#define eps 1e-8
#define lson (pos << 1)
#define rson (pos << 1 | 1)

template<class T> void checkMax(T &a, T b){a = max(a, b);}
template<class T> void checkMin(T &a, T b){a = min(a, b);}
const int N = 105;
const int M = 1005;
int n, P, Q, h[N], v[N], dp[N][M];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, cas = 1, i, j, k;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d%d", &P, &Q, &n);
        for(i = 1; i <= n; i++)
            scanf("%d%d", &h[i], &v[i]);
        memset(dp, -1, sizeof(dp));
        dp[0][1] = 0;
        for(i = 0; i < n; i++)
        {
            for(j = 0; j < M; j++)
            {
                if(dp[i][j] != -1)
                {
                    int cnt = (h[i + 1] + Q - 1) / Q;
                    checkMax(dp[i + 1][j + cnt], dp[i][j]);
                    for(k = 0; k < cnt; k++)
                    {
                        int left = (h[i + 1] - k * Q + P - 1) / P;
                        if(j + k >= left)
                        checkMax(dp[i + 1][j + k - left], dp[i][j] + v[i + 1]);
                    }
                }
            }
        }
        int ans = 0;
        for(i = 0; i < M; i++)
            checkMax(ans, dp[n][i]);
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
