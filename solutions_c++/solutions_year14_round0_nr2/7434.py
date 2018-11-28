
#include <cstdio>
#include <iostream>
using namespace std;

int main() {
	int testsCount;
	cin >> testsCount;
	for (int test = 1; test <= testsCount; ++test) {
		double C, F, X;
		cin >> C >> F >> X;
		double res = X / 2;
		double cookiesPerSecond = 2.0;
		double t = 0.0;
		for (int farms = 1; farms <= 100000; ++farms) {
			double dt = C / cookiesPerSecond;
			t += dt;
			cookiesPerSecond += F;
			res = min(res, t + X / cookiesPerSecond);
		}
		printf("Case #%d: %.7lf\n", test, res);
	}
	return 0;
}