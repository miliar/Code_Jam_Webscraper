#include <iostream>
#include <fstream>
#include <cstdio>
#include <algorithm>
#include <iomanip>

using namespace std;

const int N = 201;

double p[N];

int main() {
#ifdef _DEBUG
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		int n, k;
		cin >> n >> k;
		double p1[N];
		for (int i = 0; i < n; i++) {
			cin >> p1[i];
		}
		sort(p1, p1 + n);

		double z = -1;

		for (int r = 0; r <= k; r++) {

			for (int i = 0; i < r; i++) {
				p[i] = p1[i];
			}

			for (int i = 0; i < k - r; i++) {
				p[i + r] = p1[n - 1 - i];
			}

				/*
			for (int i = 0; i < k / 2; i++) {
				p[i] = p1[i];
				p[i + k / 2] = p1[i + n - k / 2];
			}*/

			double dp[N][N];
			memset(dp, 0, N*N*sizeof(double));

			dp[0][0] = 1;

			for (int i = 1; i <= k; i++) {
				double pp = p[i - 1];
				dp[i][0] = dp[i - 1][0] * (1 - pp);
				for (int j = 1; j <= k; j++) {
					dp[i][j] = dp[i - 1][j - 1] * pp + dp[i - 1][j] * (1 - pp);
				}
			}
			z = max(z, dp[k][k / 2]);
			//cout << fixed << dp[k][k / 2] << endl;
		}
		cout << fixed << z << endl;
	}
	return 0;
}