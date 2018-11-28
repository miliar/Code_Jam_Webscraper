#include <cstdio>
#include <algorithm>

using namespace std;

double a[256];
double d[256];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc, tcn;
	scanf("%d", &tcn);
	for (tc = 1; tc <= tcn; tc++) {
		double r = 0.0;
		int i, j, k, n, m;
		scanf("%d%d", &n, &m);
		for (i = 0; i < n; i++) scanf("%lf", &a[i]);
		sort(a, a + n);
		for (k = 0; k <= m; k++) {
			d[0] = 1.0;
			for (i = 1; i <= m; i++) d[i] = 0;
			for (i = 0; i < k; i++) {
				for (j = m; j; j--) {
					d[j] *= 1 - a[i];
					d[j] += d[j - 1] * a[i];
				}
				d[0] *= 1 - a[i];
			}
			for (i = n - m + k; i < n; i++) {
				for (j = m; j; j--) {
					d[j] *= 1 - a[i];
					d[j] += d[j - 1] * a[i];
				}
				d[0] *= 1 - a[i];
			}
			r = max(r, d[m / 2]);
		}
		printf("Case #%d: %.12f\n", tc, r);
	}
}