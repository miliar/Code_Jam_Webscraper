#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> bool chmin(T1 &a, T2 b) { if (b < a) { a = b; return true; } return false; }
template<class T1, class T2> bool chmax(T1 &a, T2 b) { if (a < b) { a = b; return true; } return false; }

void solve() {
	int n, K;
	cin >> n >> K;

	vector<double> p(n);
	for (int i = 0; i < n; i++) cin >> p[i];

	double ans = -1e100;
	for (int ii = 0; ii < 1 << n; ii++) if (__builtin_popcount(ii) == K) {
		vector<double> q;
		for (int i = 0; i < n; i++) if (ii & 1 << i) q.push_back(p[i]);

		static double dp[50][50]; // pos, yes
		fill_n(*dp, 50 * 50, 0);
		dp[0][0] = 1;

		for (int i = 0; i < K; i++) {
			for (int j = 0; j < 40; j++) {
				// yes
				dp[i + 1][j + 1] += dp[i][j] * q[i];

				// no
				dp[i + 1][j] += dp[i][j] * (1 - q[i]);
			}
		}
		chmax(ans, dp[K][K / 2]);
	}
	printf("%.20f\n", ans);
}

int main() {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
		solve();
	}
}