#include <cstdio>
#include <iostream>
#include <algorithm>

const int nPrime = 12;
const int Prime[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};

int T, n, k, a[11];

int main() {
	std::cin >> T;
	for (int cs = 1; cs <= T; cs++) {
		printf("Case #%d:\n", cs);
		std::cin >> n >> k;
		for (int i = 0; i < (1 << n - 2) && k; i++) {
			bool check = true;
			for (int base = 2; base <= 10; base++) {
				a[base] = 0;
				for (int p = 0; p < nPrime; p++) {
					int tmp = i, MOD = Prime[p];
					long long result = 1;
					for (int j = n - 3; j >= 0; j--) {
						result = (result * base + ((i >> j) & 1)) % MOD;
					}
					result = (result * base + 1) % MOD;
					if (result == 0) {
						a[base] = MOD;
						break;
					}
				}
				if (a[base] == 0) {
					check = false;
					break;
				}
			}
			if (check) {
				printf("1");
				for (int j = n - 3; j >= 0; j--) {
					printf("%d", (i >> j) & 1);
				}
				printf("1");
				for (int j = 2; j <= 10; j++) {
					printf(" %d", a[j]);
				}
				puts("");
				k--;
			}
		}
		//printf("%d\n", k);
	}
	return 0;
}
