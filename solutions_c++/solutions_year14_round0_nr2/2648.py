#include <cstdio>
#include <iostream>

int main() {
	int test;
	scanf("%d", &test);
	for (int t = 1; t <= test; ++ t) {
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		
		double answer = 1E30;
		double current = 0;
		for (int n = 0; n <= 100000; ++ n) {
			answer = std::min(answer, current + x / (2 + n * f));
			current += c / (2 + n * f);
		}
		printf("Case #%d: %.10f\n", t, answer);
	}
	return 0;
}
