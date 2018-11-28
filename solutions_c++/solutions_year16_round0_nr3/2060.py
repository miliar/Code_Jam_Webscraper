#include <bits/stdc++.h>

typedef long long Int64;

Int64 prime[30] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};

Int64 getFactor(Int64 state, Int64 base) {
	for (Int64 i = 0; i < 12; i ++) {
		Int64 s = state;
		Int64 t = 1, r = 0;
		while (s > 0) {
			r += t * (s & 1);
			r %= prime[i];
			s >>= 1;
			t *= base;
			t %= prime[i];
		}
		if (r == 0) {
			return prime[i];
		}
	}
	return -1;
}

void work() {
	Int64 cnt = 0;
	for (Int64 s = 0; s < (1LL << 30); s ++) {
		Int64 state = (1LL << 31) + (s << 1) + 1;
		bool flag = true;
		std::vector<Int64> vec;
		for (Int64 i = 2; i <= 10; i ++) {
			Int64 t = getFactor(state, i);
			if (t == -1) {
				flag = false;
				break;
			} else {
				vec.push_back(t);
			}
		}
		if (flag) {
			if (++cnt > 500) {
				break;
			}
			for (Int64 i = 31; i >= 0; i --) {
				printf("%lld", (state >> i) & 1);
			}
			printf(" ");
			for (Int64 i = 0; i < (Int64)vec.size(); i ++) {
				printf("%lld ", vec[i]);
			}
			printf("\n");
		}
	}
}

int main() {
	freopen("c.in", "r", stdin);
	freopen("c1.out", "w", stdout);
	
	printf("Case #1:\n");
	work();
	
	return 0;
}
