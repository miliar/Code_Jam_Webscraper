#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

const int all = (1 << 10) - 1;
int T, N;

int update(long long cur, int flags) {
	while (cur) {
		flags |= (1 << (cur % 10));
		cur /= 10;
	}
	return flags;
}

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		scanf("%d", &N);
		
		printf("Case #%d: ", test);
		
		if (N == 0) {
			puts("INSOMNIA");
			continue;
		}

		int flags = 0;
		long long cur = 0;

		while (flags != all) {
			cur += N;
			flags = update(cur, flags);
		}

		printf("%lld\n", cur);
	}

	return 0;
}
