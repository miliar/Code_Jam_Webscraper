#include <cstdio>

using std::scanf;
using std::printf;

const int L = 100;

static int testcase(const char *S) {
	int flips = 0;
	int i;
	for(i = 1; S[i]; ++i)
		flips += S[i - 1] != S[i];
	return flips + (S[i - 1] == '-');
}

static void testcase(int t) {
	char S[L + 1];
	scanf("%s", S);
	printf("Case #%d: %d\n", t, testcase(S));
}

int main() {
	int T;
	scanf("%i", &T);
	for(int t = 1; t <= T; ++t)
		testcase(t);
}
