#include <bits/stdc++.h>

using namespace std;

bool isPrime(long long num) {
	for (long long i = 2; i <= sqrt(num); i++) {
		if (num % i == 0) {
			return false;
		}
	}
	return true;
}

long long toBase(long long num, int base) {
	long long ret = 0;
	long long mult = 1;
	while (num != 0) {
		ret += (num % 10) * mult;
		mult *= base;
		num /= 10;
	}
	return ret;
}

int main() {
	freopen("coinjam.in", "r", stdin);
	freopen("coinjam.out", "w", stdout);
	int tc, N, J;
	scanf("%d", &tc);
	for (int i = 0; i < tc; i++) {
		printf("Case #%d:\n", i + 1);
		int ctr = 0;
		scanf("%d %d", &N, &J);
		for (long long j = 32769; (j < 65536) && (ctr < J); j += 2) {
			bool isJamCoin = true;
			char tmp[17];
			itoa(j, tmp, 2);
			long long J = atoll(tmp);
			long long result;
			for (int k = 2; k <= 10; k++) {
				result = toBase(J, k);
				if (isPrime(result)) {
					isJamCoin = false;
					break;
				}
			}
			if (isJamCoin) {
				ctr++;
				cout << J;
	
				for (int k = 2; k <= 10; k++) {
					result = toBase(J, k);
					for (long long l = 2; l <= sqrt(result); l++) {
						if (result % l == 0) {
							printf(" %lld", l);
							break;
						}
					}
				}
 				printf("\n");
			}
		}
	}
}
