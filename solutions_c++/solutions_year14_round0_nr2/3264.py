#include <iostream>
#include <stdio.h>
using namespace std;

int T;
double C, F, X;
double targetv;

int main() {
	scanf("%d", &T);
	int cas = 0;
	while (T --) {
		scanf("%lf%lf%lf", &C, &F, &X);
		targetv = 1.0 * F * (X - C) / C;
		double _time = 0.0;
		double v = 2.0;
		while (v < targetv) {
			_time += 1.0 * C / v;
			v += 1.0 * F;
		}
		_time += 1.0 * X / v;
		printf("Case #%d: %.7f\n", ++cas, _time);
	}
	return 0;
}
