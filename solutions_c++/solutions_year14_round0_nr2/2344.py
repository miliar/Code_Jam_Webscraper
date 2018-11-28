#include <cstdio>

using namespace std;

int main() {
	int t;
	double c, f, x, y, r;

	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%lf %lf %lf", &c, &f, &x);
		y = 0;
		r = 2;

		while ((x - c) * (r + f) > x * r) {
			y += c / r;
			r += f;
		}

		y += x / r;

		printf("Case #%d: %.7lf\n", i, y);
	}
}
