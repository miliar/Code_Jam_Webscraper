#include <algorithm>
#include <cstring>
#include <cstdio>

void solve(int test) {
	double c, f, x;
	scanf("%lf%lf%lf", &c, &f, &x);
	double ct = 0.;
	double ans = 1. / 0.;
	double v = 2.;
	while (ct < ans) {
		ans = std::min(ans, ct + x / v);
		ct += c / v;
		v += f;
	}
	printf("Case #%d: %.20lf\n", test, ans);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		solve(test);
	}
}
