#include <cstdio>
using namespace std;

int T, N;
int mask;

int main() {
	scanf("%d", &T);
	for (int it = 1; it <= T; it++) {
		scanf("%d", &N);
		mask = 0;
		for (int i = 1; i <= 1000000; i++) {
			long long value = 1LL * i * N;
			while (value > 0) {
				mask |= (1 << (value % 10));
				value /= 10;
			}
			if (mask == (1 << 10) - 1) {
				printf("Case #%d: %lld\n", it, 1LL * i * N);
				break;
			}
		}
		if (mask != (1 << 10) - 1) {
			printf("Case #%d: INSOMNIA\n", it);			
		}
	}
	return 0;
}