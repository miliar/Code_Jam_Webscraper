#include <cstdio>

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int no = 1; no <= T; ++no) {
		double ans = 1e20;
		double v = 2, c, f, x, t = 0;
		scanf("%lf%lf%lf", &c, &f, &x); 
		for (int i = 0; i < 100000; ++i) {
			if (t + x / v < ans) ans = t + x / v;
			t += c / v;
			v += f;
		}
		printf("Case #%d: %.7f\n", no, ans);
	}
}