#include<iostream>
using namespace std;

int main() {
	int testcases;
	double c, f, x;
	scanf("%d", &testcases);
	for (int test = 0; test < testcases; test++) {
		scanf("%lf %lf %lf", &c, &f, &x);
		double t = 0;
		double v = 2;
		while ((x - c) * (v + f) > v * x) {
			t += c / v;
			v += f;
		}
		printf("Case #%d: %.7lf\n", test + 1, x / v + t);
	}
	return 0;
}