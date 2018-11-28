#include <stdio.h>
#include <string.h>
#define EPS 1.0e-9
#define MAXIMO 100100

double tempo[100200], soma[100200];

int cmp(double a, double b) {
	if (a - b >= -EPS && a - b <= EPS) return 0;
	if (a < b) return -1;
	return 1;
}

int main() {
	int T;
	scanf(" %d", &T);
	for (int _42=1; _42 <= T; _42++) {
		double C, F, X;
		scanf(" %lf %lf %lf", &C, &F, &X);
		tempo[0] = 0;
		soma[0] = 0;
		for (int i = 1; i <= MAXIMO; i++) {
			tempo[i] = C/(2 + (i-1)*F);
			soma[i] = soma[i-1] + tempo[i];
		}
		double ans = X/2.0;
		for (int i = 1; i <= MAXIMO; i++) {
			double total = X/(2 + i*F) + soma[i];
			if (cmp(ans, total) > 0) {
				ans = total;
			}
		}

		printf("Case #%d: %.7f\n", _42, ans);
	}

	return 0;
}
