#include <cstdio>

#define EPS 1e-8

int isEqualDouble(double a, double b) {
	if (-EPS <= a - b && a - b <= EPS) {
		return 1;
	}
	if (-EPS <= a && a <= EPS) return 0;
	if (-EPS <= b && b <= EPS) return 0;
	return (-EPS <= (a - b) / a && (a - b) / a <= EPS)
	    || (-EPS <= (a - b) / b && (a - b) / b <= EPS);
}

double maxDouble(double a, double b) {
	if (a > b) return a;
	return b;
}

void calc() {
	int n;
	double vF, xF;
	double r[2], x[2];

	scanf("%d %lf %lf", &n, &vF, &xF);

	if (n == 1) {
		scanf("%lf %lf", &r[0], &x[0]);
		if (isEqualDouble(xF, x[0])) {
			printf("%.8lf\n", vF / r[0]);
		} else {
			printf("IMPOSSIBLE\n");
		}
	} else if (n == 2) {
		scanf("%lf %lf", &r[0], &x[0]);
		scanf("%lf %lf", &r[1], &x[1]);

		if (isEqualDouble(x[0], x[1])) {
			if (!isEqualDouble(x[0], xF)) {
				printf("IMPOSSIBLE\n");
			} else {
				printf("%.8lf\n", vF / (r[0] + r[1]));
			}
		} else {

			double v0 = vF * (xF - x[1]) / (x[0] - x[1]);
			double v1 = vF - v0;

			if (   (!isEqualDouble(v0, 0) && v0 < 0)
				|| (!isEqualDouble(v1, 0) && v1 < 0)
				|| (!isEqualDouble(v0, vF) && v0 > vF)
				|| (!isEqualDouble(v1, vF) && v1 > vF)
				) {
				printf("IMPOSSIBLE\n");
			} else {
				printf("%.8lf\n", maxDouble(v0 / r[0], v1 / r[1]));
			}
		}
	}
}

int main() {
	int testcase;
	int t;

	scanf("%d", &testcase);
	for (t = 1; t <= testcase; t++) {
		printf("Case #%d: ", t);
		calc();
	}

	return 0;
}