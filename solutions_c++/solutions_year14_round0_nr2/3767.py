#include <cstdio>
#include <cmath>

double x, f, c;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int qwe;
	scanf("%d", &qwe);
	for (int t = 1; t <= qwe; t++) {
		scanf("%lf%lf%lf", &c, &f, &x);
		int k = ceil(x / c - 2.0 / f - 1 - 1e-9);
		if (k < 0) k = 0;
		double ans = 0.0;
		for (int i = 0; i < k; i++)
			ans += c / (2 + f * (double)i);
		ans += x / (2 + (double)k * f);
		printf("Case #%d: %.7lf\n", t, ans);
	}
	return 0;
}
