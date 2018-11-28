#include <iostream>
#include <stdio.h>

double MIN(double a, double b) {
	if (a - b < 0) {
		return a;
	} else {
		return b;
	}
}

int main() {
	int t;
	std::cin >> t;
	int count = 1;
	while(t--) {
		double C, X, F;
		std::cin >> C >> F >> X;
		double r = 2;
		double max = X / r;
		double sum = C / r;
		while (true) {
			r += F;
			if (sum > max) {
				break;
			}
			max = MIN(max, sum + X/r);
			sum += C/r;
		}
		printf("Case #%d: %.7f\n", count, max);
		count ++;
	}
}
