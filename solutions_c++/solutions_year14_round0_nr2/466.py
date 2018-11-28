#include <cstdio>
#include <algorithm>

using namespace std;

double gao(double c, double f, double x) {
	const double EPS = 1e-8;
	double speed = 2;
	double ret = 0;
	while (x / speed >= EPS) {
		if (c / speed + x / (speed + f) < x / speed) {
			ret += c / speed;
			speed += f;
		} else {
			return ret + x / speed;
		}
	}

	return ret + x / speed;
}

int main() {
	int Tc;
	double c, x, f;
	scanf("%d", &Tc);
	for (int re = 1; re <= Tc; ++re) {
		scanf("%lf%lf%lf", &c, &f, &x);
		printf("Case #%d: %.8lf\n", re, gao(c, f, x));
	}
	return 0;
}