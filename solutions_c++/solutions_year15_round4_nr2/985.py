#include <bits/stdc++.h>

using namespace std;

//const double EPS = 1e-8;

int main() {
	int t;
	scanf("%d", &t);
	for(int kase = 1; kase <= t; kase++) {
		int n;
		double V, X;
		scanf("%d%lf%lf", &n, &V, &X);

		if(n == 1) {
			double r, x;
			scanf("%lf%lf", &r, &x);
			if(x != X)	printf("Case #%d: IMPOSSIBLE\n", kase);
			else	printf("Case #%d: %.9f\n", kase, V/r);
		}
		else {
			double r0, x0, r1, x1;
			scanf("%lf%lf%lf%lf", &r0, &x0, &r1, &x1);
			if(x0 > x1) {
				swap(x0, x1);
				swap(r0, r1);
			}

			if(x0 > X || x1 < X) {
				printf("Case #%d: IMPOSSIBLE\n", kase);
				continue;
			}

			if(x0 == X && x1 != X) {
				printf("Case #%d: %.9f\n", kase, V/r0);
				continue;
			}
			if(x1 == X && x0 != X) {
				printf("Case #%d: %.9f\n", kase, V/r1);
				continue;
			}
			if(x0 == X && x1 == X) {
				printf("Case #%d: %.9f\n", kase, V/(r0+r1));
				continue;
			}

			double a = x1-X, b = X-x0;
			printf("Case #%d: %.9f\n", kase, max(V*(x1-X)/(x1-x0)/r0, V*(X-x0)/(x1-x0)/r1));
		}
	}

	return 0;
}
