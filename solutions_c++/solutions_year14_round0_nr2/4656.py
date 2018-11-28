#include <cstdio>
#include <cstdlib>
#include <cstring>

int T;
double C, F, X;

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%lf%lf%lf", &C, &F, &X);
		double t = 0, P = 2;
		double ans = X / P;
		for (int k = 0; k <= 50000; ++k) {
			double temp = X / P;
			if (t + temp < ans) ans = t + temp;
			t += C / P;
			P += F;
		}
		printf("Case #%d: %.8f\n", tc, ans);
	}
	return 0;
}