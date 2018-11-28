#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;


double dp[250][250];

double P[250];

void solve() {
    /*int N, K;
    scanf("%d%d", &N, &K);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            dp[i][j] = 0;
        }
    }
    dp[0][0] = 1;
    for (int i = 0; i < N; ++i) {
        scanf("%lf", &P[i]);
    }
    for (int i = 0; i < N; ++i) {
        for (int k = N; k > 0; --k) {
            for (int j = k; j >= 0; --j) {
                double p = dp[k - 1][j] * (1 - P[i]);
                if (j > 0) {
                    p += dp[k - 1][j - 1] * P[i];
                }
                dp[k][j] = max(dp[k][j], p);
            }
        }
    }
    printf("%.9f\n", dp[K][K/2]);*/
    int N, K;
    scanf("%d%d", &N, &K);
    for (int i = 0; i < N; ++i) {
        scanf("%lf", &P[i]);
    }
    double ans = 0;
    for (int msk = 0; msk < (1 << N); ++msk) {
        int cnt = 0;
        for (int i = 0; i < N; ++i) {
            if (msk & (1 << i)) {
                ++cnt;
            }
        }
        if (cnt != K)
            continue;
        dp[0][0] = 1;
        cnt = 0;
        for (int i = 0; i < N; ++i) {
            if ((msk & (1 << i)) == 0) {
                continue;
            }
            ++cnt;
            for (int j = 0; j <= cnt; ++j) {
                dp[cnt][j] = 0;
                if (j > 0) {
                    dp[cnt][j] += dp[cnt - 1][j - 1] * P[i];
                }
                dp[cnt][j] += dp[cnt - 1][j] * (1 - P[i]);
            }
        }
        ans = max(ans, dp[K][K / 2]);
    }
    printf("%.9f\n", ans);

}

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        solve();
    }
    return 0;
}