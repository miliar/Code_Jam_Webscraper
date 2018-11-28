#include <iostream>
#include <string>

#define MAXN 205

using namespace std;

int tests, n, k;
long double p[MAXN], pp[MAXN], ans, tmp, tmp2, dp[MAXN][MAXN];

int main() {
	cin >> tests;
	for (int test = 1 ; test <= tests ; test ++) {
		cout << "Case #" << test << ": ";
		cin >> n >> k;
		for (int i = 0 ; i < n ; i ++) cin >> p[i];
			/*
		sort(p, p + n);
		int j = 0;
		ans = 0;
		for (int i = 0 ; i < n ; i ++) if (i < k / 2 || i + k / 2 >= n) pp[j ++] = p[i];
		for (int i = 0 ; i <= k ; i ++) {
			for (int j = 0 ; j <= k ; j ++) {
				dp[i][j] = 0;
			}
		}
		dp[0][0] = 1;
		for (int i = 1 ; i <= k ; i ++) {
			for (int j = 0 ; j <= k ; j ++) {
				if (j >= 1) dp[i][j] += dp[i - 1][j - 1] * pp[i - 1];
				dp[i][j] += dp[i - 1][j] * (1 - pp[i - 1]);
			}
		}
		cout << dp[k][k/2] << endl;
		*/
		/*while (n > k) {
			int ind = 0;
			long double maxx = 0;
			for (int ii = 0 ; ii < n ; ii ++) {
				for (int i = 0 ; i <= n ; i ++) {
					for (int j = 0 ; j <= k ; j ++) {
						dp[i][j] = 0;
					}
				}
				dp[0][0] = 1;
				for (int i = 1 ; i <= n ; i ++) {
					for (int j = 0 ; j <= k ; j ++) {
						if (i == ii + 1) {
							dp[i][j] = dp[i - 1][j];
						} else {
							if (j >= 1) dp[i][j] += dp[i - 1][j - 1] * p[i - 1];
							dp[i][j] += dp[i - 1][j] * (1 - p[i - 1]);
						}
					}
				}
				if (dp[n][k/2] > maxx) {
					maxx = dp[n][k/2];
					ind = ii;
				}
			}
			//printf("XXXXX %d\n", ind);
			p[ind] = p[-- n];
		}
		//cout << "IIII " << p[0] << " XXXX " << p[1] << endl;
		for (int i = 0 ; i <= k ; i ++) {
			for (int j = 0 ; j <= k ; j ++) {
				dp[i][j] = 0;
			}
		}
		dp[0][0] = 1;
		for (int i = 1 ; i <= k ; i ++) {
			for (int j = 0 ; j <= k ; j ++) {
				if (j >= 1) dp[i][j] += dp[i - 1][j - 1] * p[i - 1];
				dp[i][j] += dp[i - 1][j] * (1 - p[i - 1]);
			}
		}
		cout << dp[k][k / 2] << endl;*/
		sort(p, p + n);
		ans = 0;
		for (int i = 0 ; i <= n - k ; i ++) {
			for (int j = 0 ; j < k ; j ++) pp[j] = p[i + j];
			for (int i = 0 ; i <= k ; i ++) {
				for (int j = 0 ; j <= k ; j ++) {
					dp[i][j] = 0;
				}
			}
			dp[0][0] = 1;
			for (int i = 1 ; i <= k ; i ++) {
				for (int j = 0 ; j <= k ; j ++) {
					if (j >= 1) dp[i][j] += dp[i - 1][j - 1] * pp[i - 1];
					dp[i][j] += dp[i - 1][j] * (1 - pp[i - 1]);
				}
			}
			ans = max(ans, dp[k][k / 2]);
		}
		for (int ii = 0 ; ii <= k ; ii ++) {
			int j = 0;
			for (int i = 0 ; i < n ; i ++) if (i < ii || i + (k - ii) >= n) pp[j ++] = p[i];
			for (int i = 0 ; i <= k ; i ++) {
				for (int j = 0 ; j <= k ; j ++) {
					dp[i][j] = 0;
				}
			}
			dp[0][0] = 1;
			for (int i = 1 ; i <= k ; i ++) {
				for (int j = 0 ; j <= k ; j ++) {
					if (j >= 1) dp[i][j] += dp[i - 1][j - 1] * pp[i - 1];
					dp[i][j] += dp[i - 1][j] * (1 - pp[i - 1]);
				}
			}
			ans = max(ans, dp[k][k / 2]);
		}
		cout << ans << endl;
	}
	return 0;
}