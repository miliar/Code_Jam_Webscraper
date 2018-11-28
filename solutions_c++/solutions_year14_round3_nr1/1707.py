#include <cstdio>

using std::scanf;
using std::printf;

static int gcd(int a, int b) {
	while(b) {
		int t = b;
		b = a % b;
		a = t;
	}
	return a;
}

static void testcase(int t) {
	int P, Q;
	scanf("%i/%i", &P, &Q);
	int f = gcd(P, Q);
	P /= f;
	Q /= f;
	if(P > Q) {
		printf("Case #%d: %s\n", t, "impossible");
		return;
	}
	int g = 0;
	while((Q & 1) == 0 && P < Q) {
		Q >>= 1;
		++g;
	}
	while((Q & 1) == 0)
		Q >>= 1;
	if(Q != 1) {
		printf("Case #%d: %s\n", t, "impossible");
		return;
	}
	printf("Case #%d: %d\n", t, g);
}

int main() {
	int T;
	scanf("%i", &T);
	for(int t = 1; t <= T; ++t)
		testcase(t);
}
