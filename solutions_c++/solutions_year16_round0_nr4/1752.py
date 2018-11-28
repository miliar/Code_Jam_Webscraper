#include <cstdio>

using std::scanf;
using std::printf;

static long long sqr(long long n) {
	return n * n;
}

static long long pow(long long n, int e) {
	return e ? e & 1 ? n * sqr(pow(n, e / 2)) : sqr(pow(n, e / 2)) : 1;
}

static void testcase(int t) {
	int K, C, S;
	scanf("%i%i%i", &K, &C, &S);
	if(S < K) {
		// nothing is impossible in the small dataset
		printf("Case #%d: %s\n", t, "IMPOSSIBLE");
	} else {
		printf("Case #%d:", t);
		for(int s = 0; s < S; ++s)
			printf(" %lld", pow(K, C - 1) * s + 1);
		putchar('\n');
	}
}

int main() {
	int T;
	scanf("%i", &T);
	for(int t = 1; t <= T; ++t)
		testcase(t);
}
