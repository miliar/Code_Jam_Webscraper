#define _CRT_SECURE_NO_WARNINGS
#include <stdint.h>
#include <stdio.h>

const uint64_t Prime[] = {
	2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
	53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
};
const uint64_t PrimeNum = sizeof(Prime) / sizeof(Prime[0]);

inline uint64_t getbit(uint64_t x, uint64_t k) {
	return (x & (1ULL << k)) >> k;
}

int main() {
	int T = 1;
	uint64_t N = 32;
	uint64_t J = 500;
	scanf("%d%llu%llu", &T, &N, &J);
	puts("Case #1:");

	for (uint64_t bits = 0; bits < (1ULL << N); bits++) {
		if (!getbit(bits, 0) || !getbit(bits, N - 1)) {
			continue;
		}

		bool ok = true;
		uint64_t ans[11] = { 0 };
		for (uint64_t base = 2; base <= 10; base++) {
			uint64_t value[PrimeNum] = { 0 };
			for (uint64_t k = 0; k < N; k++) {
				for (uint64_t i = 0; i < PrimeNum; i++) {
					value[i] *= base;
					value[i] += getbit(bits, N - 1 - k);
					value[i] %= Prime[i];
				}
			}
			bool find = false;
			for (uint64_t i = 0; i < PrimeNum; i++) {
				if (value[i] == 0) {
					ans[base] = Prime[i];
					find = true;
					break;
				}
			}
			if (!find) {
				ok = false;
				break;
			}
		}
		if (ok) {
			for (uint64_t k = 0; k < N; k++) {
				printf("%llu", getbit(bits, N - 1 - k));
			}
			for (int i = 2; i <= 10; i++) {
				printf(" %llu", ans[i]);
			}
			putchar('\n');
			if (--J == 0) {
				break;
			}
		}
	}

	return 0;
}
