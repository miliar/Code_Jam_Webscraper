#include <cstdio>
#include <string.h>
#include <cstring>
double eps = 1e-12;
int a[30][30], b[30][30], c[20];
int n, m, testnum;

double ans, ans1, nx, nf, nc, now, already;
int rbn(double s) {
	if (s > eps) return 1;
	if (s < -eps) return -1;
	return 0;
}
int main() {
	freopen("B-large.in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testnum);
	for (int tt = 1; tt <= testnum; tt++) {
		scanf("%lf%lf%lf", &nc, &nf, &nx);
		now = 2;
		already = 0;
		ans1 = nx / now;
		while (1) {
			ans = nx / now + already;
			//printf("%.7lf   %.7lf\n", ans, ans1);
			if (rbn(ans - ans1) > 0) break;
			already += nc / now;
			now += nf;
			ans1 = ans;
		}
		printf("Case #%d: %.7lf\n", tt, ans1);

	}
	return 0;
}