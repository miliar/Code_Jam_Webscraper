#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
using namespace std;

int get_mask(int n) {
	int ret = 0;
	while (n) {
		ret |= (1 << (n % 10));
		n /= 10;
	}
	return ret;
}

int main() {
	int tests;
	scanf("%d", &tests);
	while (tests--) {
		static int testCount = 0;
		printf("Case #%d: ", ++testCount);

		int n;
		scanf("%d", &n);
		if (n == 0) {
			printf("INSOMNIA\n");
		} else {
			int mask = 0, cur = 0;
			for (; mask != (1 << 10) - 1; cur += n) {
				mask |= get_mask(cur);
			}
			printf("%d\n", cur - n);
		}
	}
	return 0;
}
