
#include <algorithm>
#include <cstdio>

double pp(double g, double *b, int n) {
	bool f = false;
	int j = 0;
	for (int i = 0; i < n; ++i) {
		if ( b[i] > g ) {
			if ( !f || b[i] < b[j] ) j = i;
			f = true;
		}
	}
	if ( !f ) j = std::min_element(b, b+n) - b;
	std::swap(b[j], b[n-1]);
	return b[n-1];
}

int ss(double *g, double *b, int n) {
	int c = 0;
	for (int i = 0; i < n; ++i) {
		double r = pp(g[i], b, n-i);
		c += r > g[i];
	}
	return c;
}

void p(int id) {
	int n;
	scanf("%d", &n);
	double g[1500], b[1500];
	for (int i = 0; i < n; ++i)
		scanf("%lf", &g[i]);
	for (int i = 0; i < n; ++i)
		scanf("%lf", &b[i]);
	printf("Case #%d: %d %d\n", id, ss(b, g, n), n - ss(g, b, n));
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
		p(i);
	return 0;
}
