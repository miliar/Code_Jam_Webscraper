#include <cstdio>
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1 ; i <= t ; ++i) {
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double a = 2, b = 0, v = x / a;
		while (true) {
			b += c / a;
			a += f;
			if (b + x / a > v) break;
			v = b + x / a;
		}
		printf("Case #%d: %.7lf\n", i, v);
	}
	return 0;
}
