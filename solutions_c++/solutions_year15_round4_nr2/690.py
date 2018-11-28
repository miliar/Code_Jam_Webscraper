#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;
const int N = 110;
double r[N], c[N];
const double eps = 1e-7;
const double inf = 1e10;

int cmp(double x, double y) {
	if (fabs(x - y) < eps) return 0;
	if (x > y) return 1;
	else return -1;
}

int main() {
    int cas = 0, n, m, x;
	scanf("%d", &x);
	while (x--) {
		double v, x;
		scanf("%d %lf %lf", &n, &v, &x);
		for (int i = 1; i <= n; i++)
			scanf("%lf %lf", &r[i], &c[i]);
		printf("Case #%d: ", ++cas);
		if (n == 1) {
			if (cmp(c[1], x) != 0)
				printf("IMPOSSIBLE\n");
			else
				printf("%.10lf\n", v / r[1]);
		} else if (n == 2) {
			if (cmp(c[1], x) > 0 && cmp(c[2], x) > 0)
				printf("IMPOSSIBLE\n");
			else if (cmp(c[1], x) < 0 && cmp(c[2], x) < 0)
				printf("IMPOSSIBLE\n");
			else {
				double ans = inf;
				if (cmp(c[1], x) == 0 || cmp(c[2], x) == 0) {
					if (cmp(c[1], x) == 0) {
						ans = min(ans, v / r[1]);
					}
					if (cmp(c[2], x) == 0) {
						ans = min(ans, v / r[2]);
					}
					if (cmp(c[1], x) == 0 && cmp(c[2], x) == 0) {
						ans = min(ans, v / (r[1] + r[2]));
					}
				} else {
					double v1 = (x * v - v * c[2]) / (c[1] - c[2]);
					double v2 = v - v1;
					ans = max(v1 / r[1], v2 / r[2]);
				}
				printf("%.10lf\n", ans);
			}
		} else {
					
		}
		
    }
    return 0;
}
