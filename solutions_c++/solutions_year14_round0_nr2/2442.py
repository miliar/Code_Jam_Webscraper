#include <cstdio>
#include <algorithm>

double c, f, x;

int main(void) {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int kase; scanf("%d", &kase); for (int _ = 1; _ <= kase; _++) {
		scanf("%lf%lf%lf", &c, &f, &x);
		double Ans = x / 2.0, now = 0;
		for (int i = 1; i <= x; i++) {
			double rate = f * (i - 1) + 2;
			now += c / rate;
			Ans = std::min(Ans, now + x / (i * f + 2));
		}
		printf("Case #%d: %.9lf\n", _, Ans);
	}
	return 0;
}

