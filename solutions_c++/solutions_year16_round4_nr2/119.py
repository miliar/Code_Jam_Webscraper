#include <bits/stdc++.h>

using namespace std;

const int N = 222;

double dp[N][N];
double p[N];
int n, K;

void solve() {
    cin >> n >> K;
    for (int i = 0; i < n; ++i) cin >> p[i];
    double ret = 0;
    int cnt;
    //for (int mask = 0; mask < 1 << n; ++mask) if (__builtin_popcount(mask) == K){
    sort(p, p + n);
    for (int it = 0; it <= K; ++it) {
        vector<double> np;
        for (int i = 0; i < it; ++i) np.push_back(p[i]);
        for (int i = 0; i < K - it; ++i) np.push_back(p[n - 1 - i]);
        for (int i = 0; i <= K; ++i) {
            for (int j = 0; j <= K; ++j) {
                dp[i][j] = 0;
            }
        }
        dp[0][0] = 1;
        for (int i = 0; i < K; ++i) {
            for (int j = 0; j <= i; ++j) {
                dp[i + 1][j] += dp[i][j] * (1 - np[i]);
                dp[i + 1][j + 1] += dp[i][j] * np[i];
            }
        }
        /*
        for (int i = 0; i <= K; ++i) {
            for (int j = 0; j <= i; ++j) {
                fprintf(stderr, "%d %d %.15f\n", i, j, dp[i][j]);
            }
        }
        */
        ret = max(ret, dp[K][K / 2]);
    }
    printf("%.15f\n", ret);
}

int main() {
    int testCount;
    cin >> testCount;
    for (int testId = 1; testId <= testCount; ++testId) {
        printf("Case #%d: ", testId);
        solve();
        fflush(stdout);
        fprintf(stderr, "%d = %.15f\n", testId, clock() / (double) CLOCKS_PER_SEC);
    }
}

