#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <vector>

uint64_t powlog(uint64_t x, uint64_t y) {
	if (y == 0) {
		return 1;
	}
	if (y == 1) {
		return x;
	}
	uint64_t tmp = powlog(x, y / 2);
	if (y % 2 == 0) {
		return tmp * tmp;
	}
	else {
		return tmp * tmp * x;
	}
}

void solve(int no) {
	uint64_t K, C, S;
	scanf("%llu%llu%llu", &K, &C, &S);
	printf("Case #%d:", no);

	if (C == 1) {
		if (K <= S) {
			for (uint64_t i = 1; i <= K; i++) {
				printf(" %llu", i);
			}
			putchar('\n');
		}
		else {
			puts(" IMPOSSIBLE");
		}
		return;
	}

	std::vector<uint64_t> ans;
	uint64_t unit = powlog(K, C-1);
	for (uint64_t x1 = 0; x1 < K; x1 += 2) {
		uint64_t x2 = x1 + 1;
		if (x2 < K) {
			ans.push_back((unit * x1 + x2) + 1);
		}
		else {
			ans.push_back((unit * x1) + 1);
		}
	}
	if (ans.size() <= S) {
		for (auto v : ans) {
			printf(" %llu", v);
		}
		putchar('\n');
	}
	else {
		puts(" IMPOSSIBLE");
	}
}

int main() {
	int T = 0;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		solve(i);
	}
}
