#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int N, K;
double P[200];
double Q[200];

double dp[201][201];

double check() {
//for (int i = 0; i < K; i++) cout << P[i] << ' ';
    dp[0][0] = 1;
    for (int i = 1; i <= K; i++) {
        for (int j = 0; j <= i; j++) {
            dp[i][j] = 0;
            if (j < i)
                dp[i][j] += dp[i-1][j] * P[i-1];
            if (j > 0)
                dp[i][j] += dp[i-1][j-1] * (1 - P[i-1]);
//cout << i << ' ' << j << ' ' << dp[i][j] << endl;
        }
    }
//cout << dp[K][K / 2] << endl;
    return dp[K][K / 2];

}

void solve() {
    cin >> N >> K;
    for (int i = 0; i < N; i++) cin >> Q[i];

    double ans = 0;
    for (int i = 0; i < (1 << N); i++) {
        int pos = 0;
        for (int j = 0; j < N; j++) {
            if ((i & (1<<j)) != 0) {
                P[pos] = Q[j];
                pos++;
            }
        }
        if (pos == K) {
            ans = max(ans, check());
        }
    }

    cout << fixed << ans << endl;
}

int main() {
    cout.precision(10);
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        cout << "Case #" << testcase << ": ";
        solve();
    }
    return 0;
}
