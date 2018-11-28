#include <bits/stdc++.h>

typedef long long Int64;

Int64 n;

void init() {
	std::cin >> n;
}

void work() {
	if (n == 0) {
		std::cout << "INSOMNIA" << std::endl;
		return ;
	}
	Int64 state = 0;
	for (Int64 k = 1; ; k ++) {
		Int64 t = k * n;
		while (t > 0) {
			state |= (1 << (t % 10));
			t /= 10;
		}
		if (state == (1 << 10) - 1) {
			std::cout << k * n << std::endl;
			return ;
		}
	}
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	Int64 testCnt;
	std::cin >> testCnt;
	for (Int64 i = 1; i <= testCnt; i ++) {
		printf("Case #%lld: ", i);
		init();
		work();
	}
	
	return 0;
}
