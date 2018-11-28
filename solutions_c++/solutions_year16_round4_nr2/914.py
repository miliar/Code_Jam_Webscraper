#include <bits/stdc++.h>

using namespace std;

int N, K;

double P[105], dp[1 << 17][20];

int main() {
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N >> K;
        for (int i = 0; i < N; ++i)
            cin >> P[i];

        double res = 0.0;
        memset(dp, 0, sizeof dp);
        dp[0][0] = 1;
        for (int mask = 1; mask < (1 << N); ++mask)
        for (int j = 0; j <= K; ++j) {
            int cnt = __builtin_popcount(mask);
            if (cnt > K) continue;
            dp[mask][j] = 0;
            for (int i = 0; i < N; ++i)
            if (mask & (1 << i)) {
                if (j > 0)
                    dp[mask][j] += dp[mask ^ (1 << i)][j] * P[i] + dp[mask ^ (1 << i)][j - 1] * (1 - P[i]);
                else
                    dp[mask][j] += dp[mask ^ (1 << i)][j] * P[i];
                break;
            }
//            cout << mask <<" "<<j << " "<<dp[mask][j] << endl;
            if (cnt == K && j == K / 2) res = max(res, dp[mask][j]);
        }

        cout << "Case #" << t << ": " << std::fixed <<setprecision(9)<< res << endl;
    }
}
