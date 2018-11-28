#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <queue>
#include <map>
#include <stack>
using namespace std;
const int MAXN = 110;
int dp[MAXN][MAXN];
int T, N, A;
int num[MAXN];
int main()
{
    freopen("A-small-attempt4.in", "r", stdin);
    freopen("A-small-attempt4.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d%d", &A, &N);
        for (int i = 1; i <= N; i++) {
            scanf("%d", num + i);
        }
        sort(num + 1, num + 1 + N);
        memset(dp, - 1, sizeof(dp));
        dp[0][0] = A;
        for (int i = 1; i <= N; i++) {
            for (int j = 0; j <= N; j++) {
                if (j >= 1 && dp[i][j - 1] != -1) {
                    dp[i][j] = max(dp[i][j], 2 * dp[i][j - 1] - 1);
                }
                if (j >= 1 && dp[i - 1][j - 1] != -1) {
                    dp[i][j] = max(dp[i][j], 2 * dp[i - 1][j - 1] - 1);
                }
                if (j >= 1 && 2 * dp[i][j - 1] - 1 > num[i]) {
                    dp[i][j] = max(dp[i][j], 2 * dp[i][j - 1] - 1 + num[i]);
                }
                if (j >= 1 && 2 * dp[i - 1][j - 1] - 1 > num[i]) {
                    dp[i][j] = max(dp[i][j], 2 * dp[i - 1][j - 1] - 1 + num[i]);
                }
                if (dp[i - 1][j] > num[i]) {
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + num[i]);
                }
                dp[i][j] = max(dp[i][j], dp[i - 1][j]);
                //printf("dp[%d][%d] = %d\n", i, j, dp[i][j]);
            }
        }
        int ret = N;
        for (int i = 0; i <= N; i++) {
            int tot = i;
            //printf("%d\n", dp[N][i]);
            for (int j = 1; j <= N; j++) {
                if (dp[N][i] <= num[j]) tot++;
            }
            ret = min(tot, ret);
        }
        printf("Case #%d: %d\n", cas, ret);
    }
    return 0;
}
