#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);
		double maxs = (x - c) * f / c, curs = 2;
		double t = 0;

		while (curs < maxs) {
			t += (c / curs);
			curs += f;
		}
		t += (x / curs);

		printf("Case #%d: %.8lf\n", i, t);
	}
	return 0;
}