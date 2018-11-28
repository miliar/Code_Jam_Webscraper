#include <iostream>
#include <stdio.h>
using namespace std;
double eps = 1e-8;
int main() {
	int t, cas = 0;
	double c, f, x;

	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%lf%lf%lf", &c, &f, &x);
		double ans;
		double now = 0;
		double r = 2;
		ans = x / 2.0;
		for (int i = 0; i <= x + 1; ++i) {
			ans = min(ans, now + x / r);
			now += c / r;
			r += f;
		}
		printf("Case #%d: %.7lf\n", cas, ans);
	}
}
