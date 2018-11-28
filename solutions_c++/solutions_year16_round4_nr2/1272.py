#include <cstdio>
#include <algorithm>
#include <map>
#include <unordered_map>

using namespace std;

const int MAXN = 200;

double pps[MAXN+2];

int n, k;

double dp[MAXN][MAXN][MAXN];
double ps[MAXN+2];

double eval() {
    const int n = k;
    for (int i = 0; i < n; ++i) {
        dp[i][i][0] = 1;
        for (int j = i+1; j <= n; ++j) {
            dp[i][j][0] = dp[i][j-1][0] * (1-ps[j-1]);
            for (int k = 1; k <= j-i; ++k) {
                dp[i][j][k] = dp[i][j-1][k] * (1-ps[j-1]) + dp[i][j-1][k-1] * ps[j-1];
            }
        }
    }

    return dp[0][k][k/2];
}

double dfs(int i, int j) {
    if (i == k)
        return eval();
    if (j == n)
        return 0;

    ps[i] = pps[j];
    double tmp = dfs(i+1, j+1);
    return max(tmp, dfs(i, j+1));
}

double solve() {
    scanf("%d%d", &n, &k);

    for (int i = 0; i < n; ++i) scanf("%lf", &pps[i]);

    return dfs(0, 0);
}

int main() {
    int T; scanf("%d", &T); for (int t = 1; t <= T; ++t) {
        printf("Case #%d: %f\n", t, solve());
    }

    return 0;
}
