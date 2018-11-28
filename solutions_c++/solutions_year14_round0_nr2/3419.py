#include <cstdio>

double C, F, X;

int main() {
	int T;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {

		scanf("%lf %lf %lf", &C, &F, &X);
		double ans = 1e20;
		double sum = 0.0;
		double rate = 2.0;
		for (int i = 0; sum < ans; ++i) {
			if (sum + X / rate < ans) {
				ans = sum + X / rate;
			}
			sum += C / rate;
			rate += F;
		}
		printf("Case #%d: %.7lf\n", t, ans);
	}
}