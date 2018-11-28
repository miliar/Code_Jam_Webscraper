#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for(int t = 1; t <= cases; ++t) {
		printf("Case #%d: ", t);
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double v = 2.0, ans = 0;
		while(c / v + x / (v + f) < x / v) {
			ans += c / v;
			v += f;
		}
		ans += x / v;
		printf("%.7lf\n", ans);
	}
	return 0;
}
