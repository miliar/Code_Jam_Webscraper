#include <cstdio>

#define RE 100
#define BASE 2.0

int main() {
	int Total;
	double C, F, X;
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &Total);
	for (int i = 0; i < Total; i++) {
		scanf("%lf %lf %lf", &C, &F, &X);
		printf("Case #%d: ", i + 1);
		double left = 0.0, right = X / BASE, result = 0;
		for (int j = 0; j < RE; j++) {
			result = (left + right) / 2;
			double time = 0, remaining = 0, rate = BASE;
			while ((time < result) && ((result - time) * rate <= X)) {
				if ((result - time - C / rate) * F > C) {
					time += C / rate;
					rate += F;
					//printf("%f %f %f %f\n", left, right, time, rate);
				} else {
					break;
				}
			}
			remaining += (result - time) * rate;
//			printf("%d %f %f %f %f %f %f\n", j, left, right, result, time, rate, remaining);
			if (remaining > X) {
				right = result;
			} else {
				left = result;
			}

		}
		printf("%.7f\n", result);
	}
	return 0;
}
