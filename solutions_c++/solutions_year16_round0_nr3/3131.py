#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long ll;

int check_prime(ll x) {
	ll sq = (ll)sqrt(x);
	if (sq * sq == x) return sq;
	int sq3 = (int)pow(x, 1.0 / 3.0) + 1;
	for (int i = 2; i <= sq3; ++i)
		if (x % i == 0) return i;
	return 0;
}

int main() {
	freopen("output.txt", "w", stdout);
	printf("Case #1:\n");
	int start = 1,
		end = 1,
		num = 0;
	int arr[11];
	int bnr[17];
	for (int i = 0; i < 15; ++i) start *= 2;
	for (int i = 0; i < 16; ++i) end *= 2;
	for (int i = start + 1; i < end && num < 50; i += 2) {
		int div = check_prime(i);
		if (div != 0) {
			arr[2] = div;
			int j = 1;
			for (int t = 0; t < 16; ++t) {
				bnr[t] = (i&j) ? 1 : 0;
				j *= 2;
			}
			bool ok = true;
			for (int ss = 3; ss <= 10; ++ss) {
				ll x = 0;
				ll deg = 1;
				for (int t = 0; t < 16; ++t) {
					x += deg * bnr[t];
					deg = deg * ss;
				}
				int divss = check_prime(x);
				if (divss == 0) {
					ok = false;
					break;
				}
				arr[ss] = divss;
			}
			if (ok) {
				++num;
				for (int t = 15; t >= 0; --t)
					printf("%d", bnr[t]);
				for (int ss = 2; ss <= 10; ++ss)
					printf(" %d", arr[ss]);
				printf("\n");
			}
		}
	}
	return 0;
}