#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	int T, c;
	double C, F, X, q, p, best;
	scanf("%d", &T);
	c = 1;
	while (T--) {
		scanf("%lf %lf %lf", &C, &F, &X);
		p = 2.0;
		q = 0;
		best = 100000;
		while (X/p + q < best) {
			best = X/p + q;
			q += C/p;
			p += F;
		}
		printf("Case #%d: %.7lf\n", c++, best);
	}
	return 0;
}
