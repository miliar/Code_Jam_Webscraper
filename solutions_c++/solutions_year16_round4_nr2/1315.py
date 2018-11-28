#include <bits/stdc++.h>
using namespace std;
double p[555];
double dp[205][205][205];
const double eps = 1e-15;
int n, k;
double a[555];
	
bool bit(int mask, int x) {
	mask &= (1 << x);
	return mask > 0;
}
double f(int n, int a, int b) {
	if (a < 0 || b < 0) return 0.0;
	if (n < 0) {
		if (a + b == 0) {
			return 1.0;
		}
		return 0.0;
	}
	if (dp[n][a][b] >= -eps) return dp[n][a][b];
	double ret = 0;
	ret = f(n - 1, a, b);
	ret = max(ret, f(n - 1, a - 1, b) * p[n] + f(n - 1, a, b - 1) * (1 - p[n]));
	dp[n][a][b] = ret;
	return ret;
}
void solve() {
	cin >> n >> k;
	for (int i = 0; i < n; ++i) {
		cin >> p[i];
	}
	double ans = 0;
	for (int m = 0; m < (1 << n); ++m) {
		int t = 0;
		for (int i = 0; i < n; ++i) {
			if (bit(m, i)) {
				a[t++] = p[i];
			}
		}
		if (t != k) continue;
		for (int i = 0; i <= k; ++i) {
			for (int j = 0; j <= k; ++j) {
				for (int t = 0; t <= k; ++t) {
					dp[i][j][t] = 0;
				}
			}
		}
		dp[0][0][0] = 1.0;
		for (int i = 0; i < k; ++i) {
			for (int j = 0; j <= i; ++j) {
				for (int t = 0; t <= i; ++t) {
					dp[i + 1][j + 1][t] += dp[i][j][t] * a[i];
					dp[i + 1][j][t + 1] += dp[i][j][t] * (1 - a[i]);
				}
			}
		}
		ans = max(ans, dp[k][k / 2][k / 2]);
	}
	
	cout.precision(15);
	cout << fixed << ans << endl;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int it = 1; it <= t; ++it) {
		cout << "Case #" << it << ": ";
		solve();
	}
	return 0;
}
