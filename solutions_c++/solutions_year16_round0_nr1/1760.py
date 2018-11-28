#include <cstdio>

using std::scanf;
using std::printf;

const int base = 10;

static void add_digits(int& d, int a) {
	while(a) {
		int m = a % base;
		a /= base;
		d |= 1 << m;
	}
}

const int all_digits = (1 << base) - 1;
const int no_digits = 0;

static void testcase(int t, int N) {
	if(N == 0) {
		printf("Case #%d: %s\n", t, "INSOMNIA");
		return;
	}
	int seen = no_digits;
	int a = N;
	for(;;) {
		add_digits(seen, a);
		if(seen == all_digits)
			break;
		a += N;
	}
	printf("Case #%d: %d\n", t, a);
}

static void testcase(int t) {
	int N;
	scanf("%i", &N);
	testcase(t, N);
}

int main() {
	int T;
	scanf("%i", &T);
	for(int t = 1; t <= T; ++t)
		testcase(t);
}
