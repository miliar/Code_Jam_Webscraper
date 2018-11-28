#include <cstdio>

int main() {
	int tests, k;
	double c, f, x, time;
	scanf("%d", &tests);
	for (int test_id = 1; test_id <= tests; test_id++) {
		scanf("%lf %lf %lf", &c, &f, &x);
		k = ((f * x - 2 * c) / (c * f));
		time = 0;
		for (int i = 0; i < k; i++)
			time += c / (2.0 + i * f);
		if (k > 0)
			time += x / (2.0 + k * f);
		else
			time += x / 2.0;
		printf("Case #%d: %.7f\n", test_id, k, time);
	}
	return 0;
}
/*
g = 2
(x - x_curr) / g <= (x - x_curr + c) / (g + f)

k farms
g = 2 + f * k
t(k) = c / 2 + c / (2 + f) + ... + c / (2 + (k - 1) * f) + x / (2 + k * f)
t(k + 1) - t(k) = c / (2 + k * f) + x / (2 + f + k * f) - x / (2 + k * f) > 0
*/