#include <iostream>
#include <cstdio>

using namespace std;

int t;
double c, f, x;
int main() {
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		cin >> c >> f >> x;
		double p = 2.0;
		double current = x / p;
		double ac = 0.0;
		while (true) {
			ac += c / p;
			double actual = ac + (x / (p+f));
			p += f;
			if (actual > current) break;
			current = actual;
		}
		printf("Case #%d: %.7f\n", i, current);
	}
	return 0;
}
