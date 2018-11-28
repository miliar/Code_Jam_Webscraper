#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

double dp[20][20];

int main() {
	int t; cin >> t;
	for (int test = 1; test <= t; ++test) {
		int n, k; cin >> n >> k;
		vector<double> department(n);
		for (int i = 0; i < n; ++i) cin >> department[i];

		double ans = 0.0;
		for (int mask = 0; mask < (1 << n); ++mask) {
			vector<int> expand;
			for (int i = 0; i < n; ++i) if (mask & (1 << i)) expand.push_back(i);
			if (expand.size() != k) continue;

			for (int i = 0; i < 20; ++i) for (int j = 0; j < 20; ++j) dp[i][j] = 0.0;
			dp[0][0] = 1.0; // 100%

			for (int i = 0; i < k; ++i) {
				double p = department[expand[i]];
				for (int j = 0; j <= i; ++j) {
					dp[i+1][j] += dp[i][j] * (1-p);
					dp[i+1][j+1] += dp[i][j] * (p);
				}
			}
			double curr = dp[k][k/2];
			ans = max(ans, curr);
		}

		cout << "Case #" << test << ": " << fixed << setprecision(9) << ans << endl;
	}
	return 0;
}