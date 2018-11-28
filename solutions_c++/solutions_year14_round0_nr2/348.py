#include <cstdio>
double c, f, x;
void solve() {
	scanf("%lf%lf%lf", &c, &f, &x);
	double now = 0, rate = 2, ans = x/2;
	while (1) {
		now += c/rate;
		rate += f;
		double tmp = now + x/rate;
		if (tmp < ans) ans = tmp;
		else break;
	}
	printf("%.7lf\n", ans);
}
int main() {
	int T; scanf("%d", &T);
	for (int _ = 1; _ <= T; _++)
		printf("Case #%d: ", _), solve();
	return 0;
}
