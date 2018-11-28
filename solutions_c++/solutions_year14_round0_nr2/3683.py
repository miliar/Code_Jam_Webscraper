#include <stdio.h>

int max(int a, int b) {
	if (a < b) {
		return b;
	}
	return a;
}

int round(double a) {
	int i = a;
	if (i > a) {
		return i - 1;
	}
	return i;
}

int main() {
	freopen ("B-large.in","r",stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		double C, F, X;
		scanf("%lf %lf %lf", &C, &F, &X);
		double kdouble = (F * X - 2 * C - F * C) / (F * C);
		int kint = round((F * X - 2 * C - F * C) / (F * C));
		int kmax = kint;
		if (kdouble - 0.0000001 <= kint && kint <= kdouble + 0.00000001) {
			kmax -= 1;
		}
		double count = 0.0;
		for (int k = 0; k <= kmax; k++) {
			count += C / (2 + F * k);
		}
		count += X / (2 + F * max(kmax + 1, 0));

		printf("Case #%d: %.7lf\n",i + 1, count);
	}

	fclose(stdout);
	return 0;
}