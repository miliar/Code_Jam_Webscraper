#include <stdio.h>
#include <cmath>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <stdlib.h>
#include <assert.h>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std;
typedef long long lint;
const double EPS = 1e-6;

double v0, x0, v1, x1, v, x;
int n;

int main() {
	int t;
	scanf("%d", &t);
	for(int cas = 1; cas <= t; cas++) {
		scanf("%d", &n);
		scanf("%lf%lf", &v, &x);
		printf("Case #%d: ", cas);

		if(n == 1) {
			scanf("%lf%lf", &v0, &x0);
			if(fabs(x0 - x) < EPS) {
				printf("%.8lf\n", v / v0);
			}
			else {
				puts("IMPOSSIBLE");
			}
		}
		else {
			scanf("%lf%lf%lf%lf", &v0, &x0, &v1, &x1);
			if(fabs(x0 - x1) < EPS) {
				if(fabs(x0 - x) < EPS) {
					printf("%.8lf\n", v / (v0 + v1));
				}
				else {
					puts("IMPOSSIBLE");
				}
				continue;
			}

			double t0 = (v * x - v * x1) / (v0 * x0 - v0 * x1);
			double t1 = (v - v0 * t0) / v1;
			if((t0 < 0 && fabs(t0) > EPS) || (t1 < 0 && fabs(t1) > EPS)) {
				puts("IMPOSSIBLE");
			}
			else {
				printf("%.8lf\n", max(t0, t1));
			}
		}
	}
	return 0;
}
