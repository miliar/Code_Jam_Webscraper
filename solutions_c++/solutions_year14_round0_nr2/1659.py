#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

const double INF = 1e10;

int main() {
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int cc, t;
	double b, c, dr, r, g, w;
	scanf("%d", & t);
	for (cc = 0; cc < t; cc++) {
		scanf("%lf %lf %lf", & c, & dr, & g);
		b = INF;
		w = 0.0;
		r = 2.0;
		while (w < b) {
			b = min(b, w + g / r);
			w += c / r;
			r += dr;
		}
		printf("Case #%d: %.7lf\n", cc + 1, b);
	}
	return 0;
}

