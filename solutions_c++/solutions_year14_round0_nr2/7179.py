// bb.cpp 
#include <iostream>
#include <cstdio>

#define s(n) scanf("%lf", &n)

int main() {
	int tc; scanf("%d", &tc);
	for(int tt = 0; tt < tc; tt++) {
		double c, f, x, r(2), t(0);
		s(c); s(f); s(x);
		
		while((x / r) > ((c / r) + (x / (r + f)))) {
			t += (c / r);
			r += f;
		}

		t += (x / r);

		printf("Case #%d: %.7f\n", tt + 1, t);
	}
	return 0;
}
