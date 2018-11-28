#include <bits/stdc++.h>

using namespace std;

int main() {
	int n, conta = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		double c,f,x;
		scanf("%lf %lf %lf", &c, &f, &x);
		double d = 2.0 + f;
		double now = x/2.0, extra = c/2.0 + (x/d);
		while (now - extra > 0.00000001) {
			now = extra;
			extra -= (x/d);
			extra += ((c/d) + x/(d + f));
			d += f;
		}
		printf("Case #%d: %.7lf\n", ++conta, now);
	}
	return 0;
}