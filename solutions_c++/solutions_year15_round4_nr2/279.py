#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <map>
#include <vector>
#include <set>
#include <cstdlib>
using namespace std;

typedef long long LL;

int n;
long double v, t;
long double r[105], c[105];

#define eps 1e-10

bool equal(long double x, long double y) {
	return (fabs(x - y) < eps);
}

int cmp(long double x, long double y) {
	if (x - y < -eps) return -1;
	if (x - y > eps) return 1;
	return 0;
}

int main() {
	int T, cases = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%Lf%Lf", &n, &v, &t);
		for (int i = 0; i < n; ++i) {
			scanf("%Lf%Lf", &r[i], &c[i]);
		}
		printf("Case #%d: ", ++cases);
		if (n == 1) {
			if (!equal(c[0], t)) {
				printf("IMPOSSIBLE\n");
				continue;
			} else {
				printf("%.9Lf\n", v / r[0]);
			}
		} else if (n == 2) {
			if ((equal(c[1], t)) || (equal(c[0], t)) || 
				((cmp(c[1], t) == -1) && ((cmp(c[0], t) == 1))) ||
				((cmp(c[1], t) == 1) && ((cmp(c[0], t) == -1)))) {
				if ((equal(c[1], t)) && (equal(c[0], t))) {
					printf("%.9Lf\n", v / (r[0] + r[1]));
					continue;
				}
				long double v0 = (t * v - c[1] * v) / (c[0] - c[1]);
				long double v1 = v - v0;
				printf("%.9Lf\n", max(v0 / r[0], v1 / r[1]));
			} else {
				printf("IMPOSSIBLE\n");
			}
		}
		//		printf("Case #%d:\n", ++cases);
	}
	return 0;
}
