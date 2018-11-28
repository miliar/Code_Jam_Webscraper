#include <cstdio>
#include <cmath>

int main(void) {
	int T;
	double C, F, X;
	double total_t;
	int n;

	scanf ("%d", &T);

	for (int i = 1; i <= T; i++) {
		scanf ("%lf%lf%lf", &C, &F, &X);

		n = (int) ceil((X-C)/C - 2.0/F);
		if (n < 0) n = 0;

		total_t = X / (n*F + 2);
		for (int j = 0; j < n; j++)
			total_t += C / (j*F + 2.0);

		printf("Case #%d: %.7lf\n", i, total_t);
		}
	return 0;
	}
