#include <cstdio>

typedef double real;

real answer() {
	real c, f, x, t = 0, m = 0, r = 2, t1, t2, remain;
	scanf("%lf%lf%lf", &c, &f, &x);
	while (m < x) {
		remain = x - m;
		t1 = remain / r;
		if (remain >= c) {
			t2 = c / r + remain / (r + f);
			if (t2 < t1) {
				t += c / r;
				r += f;
				continue;
			}
		}
		t += t1;
		m += remain;
	}

	return t;
}

int main() {
	int n = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		printf("Case #%d: %.7f\n", i + 1, answer());
	}
}