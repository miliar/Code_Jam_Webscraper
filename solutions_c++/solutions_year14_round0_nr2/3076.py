#include <cstdio>

int main() {
	int N;
	scanf("%d", &N);
	for (int T = 1; T <= N; T++) {
		double C, F, X;
		scanf("%lf %lf %lf", &C, &F, &X);

		double t = 0;
		double r = 2;
		double min = X/r;
		for (int f = 1; f <= (int) X; f++) {
			t += C/r;
			r += F;
			double val = t+X/r;
			if (val < min) min = val;
		}

		printf("Case #%d: %.7f\n", T, min);
	}
	return 0;
}
