#include <iostream>
#include <algorithm>
#include <string>
#include <iomanip>
using namespace std;

double p[256], fwd_dp[256][256], rev_dp[256][256];

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; i++)
			cin >> p[i];
		
		sort(p, p + n);

		fwd_dp[0][0] = 1.0;
		for (int i = 1; i <= n; i++) {
			for (int j = 0; j <= i; j++) {
				fwd_dp[i][j] = 0.0;
				if (j < i)
					fwd_dp[i][j] += fwd_dp[i - 1][j] * (1.0 - p[i - 1]);
				if (j > 0)
					fwd_dp[i][j] += fwd_dp[i - 1][j - 1] * p[i - 1];
				// cout << i << j << fwd_dp[i][j] << endl;
			}
		}

		rev_dp[n][0] = 1.0;
		for (int i = n - 1; i >= 0; i--) {
			for (int j = 0; j <= n - i; j++) {
				rev_dp[i][j] = 0.0;
				if (j < n - i)
					rev_dp[i][j] += rev_dp[i + 1][j] * (1.0 - p[i]);
				if (j > 0)
					rev_dp[i][j] += rev_dp[i + 1][j - 1] * p[i];
				// cout << i << j << rev_dp[i][j] << endl;
			}
		}

		double ans = 0.0;
		for (int i = 0; i <= k; i++) {
			double nans = 0.0;
			for (int j = 0; j <= k / 2; j++) {
				if (j <= i && k / 2 - j <= k - i) {
					// cout << i << j << k << endl;
					nans += fwd_dp[i][j] * rev_dp[n - (k - i)][k / 2 - j];
				}
			}
			ans = max(ans, nans);
		}
		cout << "Case #" << t << ": ";
		cout << setprecision(12) << ans << endl;
	}

	return 0;
}
