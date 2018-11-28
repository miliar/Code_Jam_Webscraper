// run: $exec < b-large.in > b-large.out
#include <iostream>
#include <iomanip>
#include <algorithm>

const int maxn = 305;
double p[maxn];
double pp[maxn];
double dp[maxn][maxn];
int n, k;

double calc(int n)
{
	dp[0][0] = 1;
	for (int i = 1; i <= n; i++)
		for (int j = 0; j <= i; j++) {
			dp[i][j] = 0;
			if (j >= 1) dp[i][j] += dp[i - 1][j - 1] * pp[i];
			dp[i][j] += dp[i - 1][j] * (1 - pp[i]);
		}
	return dp[n][n/2];
}

int main()
{
	int T; std::cin >> T;
	for (int ti = 1; ti <= T; ti++) {
		std::cout << "Case #" << ti << ": ";
		std::cin >> n >> k;
		for (int i = 1; i <= n; i++) std::cin >> p[i];
		std::sort(p + 1, p + n + 1);

		double ans = 0.0;
		for (int i = 0; i <= k; i++) {
			int m = 0;
			for (int j = 1; j <= i; j++) pp[++m] = p[j];
			for (int j = 1; j <= k - i; j++) pp[++m] = p[n - j + 1];
			ans = std::max(ans, calc(k));
		}
		std::cout << std::fixed << std::setprecision(8) << ans << '\n';
	}
}

