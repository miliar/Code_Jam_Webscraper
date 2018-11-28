#include <cstdio>

using std::printf;
using std::scanf;

const int M = 1000;

static int testcase(const char *S) {
	int invited = 0;
	int standing = 0;
	for(int k = 0; S[k]; ++k) {
		int Sk = S[k] - '0';
		if(Sk == 0)
			continue;
		if(standing >= k) {
			standing += Sk;
			continue;
		}
		int deficit = k - standing;
		invited += deficit;
		standing += deficit;
		standing += Sk;
	}
	return invited;
}

static void testcase(int t) {
	char S[M + 1 + 1];
	scanf("%*d%s", S);
	printf("Case #%d: %d\n", t + 1, testcase(S));
}

int main() {
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; ++t)
		testcase(t);
}
