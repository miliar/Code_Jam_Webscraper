
#include <cstdio>

void p(int id) {
	double c, f, x;
	scanf("%lf%lf%lf", &c, &f, &x);
	double p = 2.0, t = c / p;
	while ( true ) {
		if ( x / (p+f) < (x-c) / p ) {
			p += f;
			t += c / p;
		} else {
			t += (x-c) / p;
			break;
		}
	}
	printf("Case #%d: %.8f\n", id, t);
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
		p(i);
	return 0;
}
