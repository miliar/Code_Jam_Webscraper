#include <bits/stdc++.h>
using namespace std;

typedef __int128 i128;
typedef long long LL;

int T;
int N, J;
LL d[16];
set <LL> S;

i128 isPrime(i128 num) {
	for (i128 i = 2; i * i <= num && i < 100000; ++i) {
		if (num % i == 0)
			return i;
	}
	return -1;
}

i128 toBaseB(i128 num, i128 B) {
	i128 base = 1, ans = 0;
	for (; num > 0; num /= i128(2)) {
		if (num % (i128)2 == 1)
			ans += base;
		base *= B;
	}
	return ans;
}

void print2(LL num, LL N) {
	for (N-- ;N >= 0; N --) {
		if (num & (1ll << N))
			putchar('1');
		else
			putchar('0');
	}
}

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; ++test) {
		printf("Case #%d:\n", test);
		scanf("%d%d", &N, &J);
		LL MOD = (1 << (N - 2));
		while (J--) {
			while (true) {
				LL num = rand() % MOD;
				num = num * 2ll + 1;
				num += 1ll << (LL)(N - 1);
				if (S.find(num) != S.end())
					continue;
				bool ok = true;
				for (int i = 2; i <= 10; ++i) {
					d[i] = (int)isPrime(toBaseB(num, i));
					if (d[i] == -1) {
						ok = false;
						break;
					}
				}
				if (ok) {
					S.insert(num);
					print2(num, N);
					for (int i = 2; i <= 10; ++i)
						printf(" %d", (int)d[i]);
					printf("\n");
					break;
				}
			}
		}
	}
	return 0;
}