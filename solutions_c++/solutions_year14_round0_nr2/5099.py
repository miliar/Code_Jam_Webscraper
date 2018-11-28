#include <iostream>
#include <stdio.h>
using namespace std;

double solve(double c, double f, double x) {
	double s = 2;
	double a0 = x/s;
	double t0 = c/s;
	while (true) {
		s += f;
		double a1 = t0 + x/s; 
		if (a1 > a0)
			break;
		a0 = a1;
		t0 += c/s;
	}
	return a0;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		printf("Case #%d: %lf\n", i, solve(c, f, x));
	}
	return 0;
}