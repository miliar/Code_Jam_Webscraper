#include<bits/stdc++.h>

using namespace std;

long double p[201], f[201][201], g[202][202];

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int n, k;
		scanf("%d %d", &n, &k);
		for (int i = 1; i <= n; i++) scanf("%Lf", p + i);
		
		k /= 2;
		
		sort(p + 1, p + n + 1);
	
		f[0][0] = 1.0;
		for (int i = 1; i <= n; i++) {
			f[i][0] = (1 - p[i]) * f[i - 1][0];
			for (int j = 1; j <= k; j++) {
				f[i][j] = f[i - 1][j] * (1 - p[i]) + f[i - 1][j - 1] * p[i];
			}
		}
		
		g[n + 1][0] = 1.0;
		for (int i = 1; i <= k; i++) g[n + 1][i] = 0.0;
		for (int i = n; i > 0; i--) {
			g[i][0] = (1 - p[i]) * g[i + 1][0];
			for (int j = 1; j <= k; j++) {
				g[i][j] = g[i + 1][j] * (1 - p[i]) + g[i + 1][j - 1] * p[i];
			}
		}
		
		long double ans = 0.0;
		for (int i = 0; i <= 2 * k; i++) {
			long double sum = 0.0;
			for (int j = 0; j <= k; j++) sum += f[i][j] * g[n + 1 + i - 2 * k][k - j];
			
			ans = max(ans, sum);
		}
		
		printf("Case #%d: %.12Lf\n", t, ans);
	}
	
	return 0;
}
