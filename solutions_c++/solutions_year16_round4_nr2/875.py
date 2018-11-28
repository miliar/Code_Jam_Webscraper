#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 101;

double a[N], b[N];
double dp[N][N];
int n, m;
double ans;

void update(double &a, double b) {
    a += b;
}
double cal() {
	memset(dp, 0, sizeof(dp));
	dp[0][0] = 1;
	for (int i = 1; i <= m; i++) {
		for (int j = 0; j < i; j++) {
			update(dp[i][j], dp[i - 1][j] * (1 - b[i]));
			update(dp[i][j + 1], dp[i - 1][j] * (b[i]));
		}
	}
	return dp[m][m / 2];
}
void test(int i, int j) {
	if (i > n) {
		if (j == m) ans = max(ans, cal());
		return;
	}
	test(i + 1, j);
	b[++j] = a[i];
	test(i + 1, j);
}
int main() {
	int t, tt;
	scanf("%d", &t);
	for (tt = 1; tt <= t; tt++) {
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; i++) scanf("%lf", &a[i]);
		ans = 0;
		test(1, 0);
		printf("Case #%d: %.10f\n", tt, ans);
	}
	return 0;
}
