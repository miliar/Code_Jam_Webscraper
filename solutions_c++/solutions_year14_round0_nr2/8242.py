#include <cstdio>
#include <algorithm>

typedef long double ld;

void solve() {
	ld c, f, x;
	scanf("%Lf%Lf%Lf", &c, &f, &x);
	ld best = 2000000000.0;
	ld currentTime = 0.0;
	ld cps = 2.0;
	bool ok = true;
	while(ok) {
		ok = false;
		// to X
		ld t = currentTime + x / cps;
		if(t < best) {
			ok = true;
			best = t;
		}
		currentTime += c / cps;
		cps += f;
		// printf("(%lf / %lf)", c, cps);
	}
	printf("%.7Lf", best);
}

int main() {
	int tests;
	scanf("%d", &tests);
	for(int test = 0; test < tests; test++) {
		printf("Case #%d: ", test + 1);
		solve();
		printf("\n");
	}
	return 0;
}
