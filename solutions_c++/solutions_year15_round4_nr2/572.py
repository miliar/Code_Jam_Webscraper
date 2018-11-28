#include <stdio.h>
#include <math.h>
#include <algorithm>

using namespace std;

int main()
{
	int dat;
	scanf("%d", &dat);
	for (int cas = 1; cas <= dat; ++cas) {
		printf("Case #%d: ", cas);
		int n;
		double v, x;
		scanf("%d%lf%lf", &n, &v, &x);
		if (n == 1) {
			double r, c;
			scanf("%lf%lf", &r, &c);
			if (fabs(x - c) < 1e-8) {
				printf("%.12f\n", v / r);
			} else {
				puts("IMPOSSIBLE");
			}
		} else {
			double r1, c1, r2, c2;
			scanf("%lf%lf%lf%lf", &r1, &c1, &r2, &c2);
			double A1 = r1, B1 = r2, C1 = v;
			double A2 = r1 * c1, B2 = r2 * c2, C2 = v * x;
			if (fabs(c1 - c2) < 1e-8) {
				if (fabs(x - c1) < 1e-8) {
					printf("%.12f\n", v / (r1 + r2));
				} else {
					puts("IMPOSSIBLE");
				}
				continue;
			}
			double x1 = (v * c2 - v * x) / (r1 * c2 - r1 * c1);
			double x2 = (v * c1 - v * x) / (r2 * c1 - r2 * c2);
			if (x1 > -1e-8 && x2 > -1e-8) {
				printf("%.12f\n", max(x1, x2));
			} else {
				puts("IMPOSSIBLE");
			}
		}
	}
}
