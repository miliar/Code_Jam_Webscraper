#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

char mask[111];

bool check(char *mask, int base, int divisor, int N) {
	int sum = 0;
	int power = 1;
	for (int i = N-1; i >= 0; --i) {
		sum = (sum + power * (mask[i] - '0')) % divisor;
		power = power * base % divisor;
	}
	return sum == 0;
}

int main(void) {


	int T = 0;
	scanf("%d", &T);
	puts("Case #1:");
	int N, J;
	scanf("%d %d", &N, &J);


	int total = 0;
	mask[N] = 0;
	for (int s = 0; s < (1<<(N/2-1)); ++s) {
		
		mask[0] = '1';
		for (int i = 0; i < N/2-1; ++i) {
			mask[i*2+1] = (s >> i & 1) + '0';
			mask[i*2+2] = (s >> i & 1) + '0';
		}
		mask[N-1] = '1';

		printf("%s", mask);

		for (int base = 2; base <= 10; ++base) {
			int ans = 0;
			if (base & 1) ans = 2;
			else ans = base+1;
			printf(" %d", ans);
			assert(check(mask, base, ans, N));
		}
		puts("");
		++total;
		if (total >= J) break;
	}

	return 0;
}