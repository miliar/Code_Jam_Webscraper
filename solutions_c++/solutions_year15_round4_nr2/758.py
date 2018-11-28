#include <bits/stdc++.h>

using namespace std;

#define EPS 1e-8

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for(int test = 1; test<=t; test++) {
		int n;
		double volume, temperature;
		scanf("%d %lf %lf", &n, &volume, &temperature);
		printf("Case #%d: ", test);
		if(n == 1) {
			double v1, t1;
			scanf("%lf %lf", &v1, &t1);
			if(fabs(t1-temperature) > EPS) {
				printf("IMPOSSIBLE\n");
			}
			else {
				printf("%.9lf\n", volume/v1);
			}
		}
		else {
			double v1, t1;
			scanf("%lf %lf", &v1, &t1);
			double v2, t2;
			scanf("%lf %lf", &v2, &t2);
			if(fabs(t1-t2) < EPS) {
				double v12, t12;
				v12 = v1+v2;
				t12 = t1;
				if(fabs(t12-temperature) > EPS) {
					printf("IMPOSSIBLE\n");
				}
				else {
					printf("%.9lf\n", volume/v12);
				}
			}
			else {
				double q1 = (volume*temperature-volume*t2)/(t1-t2);
				double q2 = volume - q1;
				if(q1 < -EPS || q2 < -EPS) printf("IMPOSSIBLE\n");
				else {
					double minimum = max(q1/v1, q2/v2);
					printf("%.9lf\n", minimum);
				}
			}
		}
	}

	return 0;
}