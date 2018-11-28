#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;

const int maxn = 500;
const int med = 250;

ld dp[maxn][maxn];
ld p[maxn]; //1 ind
ld q[maxn];

ld count (int n) {
    dp[0][med] = 1.0;
    for (int i = 1; i <= n; ++i) {
        for (int j = -n; j <= n; ++j) {
            dp[i][med + j] = p[i] * dp[i - 1][med + j - 1] + (1.0 - p[i]) * dp[i - 1][med + j + 1];
        }
    }
    return dp[n][med];
}

void Solve() {
    int n, k;
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; ++i) scanf("%Lf", &q[i]);
    sort(q, q + n);
    for (int i = 0; i < k; ++i) p[i + 1] = q[i];
    ld ans = count(k);
    for (int i = k; i > 0; --i) {
        p[i] = q[n - k - 1 + i];
        ans = max(ans, count(k));
    }
    printf("%.10Lf\n", ans);
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t; scanf("%d", &t);
    for(int i = 1; i <= t; ++i) {
        printf("Case #%d: ", i);
        Solve();
    }
}
