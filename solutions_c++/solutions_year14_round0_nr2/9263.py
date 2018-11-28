#include <cstdio>
using namespace std;

int main() {
	int t, T;
	double a, b, c, d, r, s, u, v;
	bool e;
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf("%lf%lf%lf", &a, &b, &c);
		r = 0;
		d = 2;
		e = false;
		while (!e) {
			s = c / d;
			u = a / d;
			v = u + (c / (d + b));
			if (s < v) {
				r += s;
				e = true;
			} else {
				r += u;
				d += b;
			}
		}
		printf("Case #%d: %.7lf\n", t, r);
	}
	return 0;
}