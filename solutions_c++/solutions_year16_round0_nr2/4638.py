#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

const int MN = 10;
bool dp[(1 << MN) + 10][2 * MN + 10] = { 0 };

int do_flip(int mask, int pos, int n) {
	int new_mask = 0;
	for (int i = pos; i < n; ++i) {
		if (!((1 << i) & mask)) {
			new_mask |= (1 << (n - i + pos - 1));
		}
	}
	for (int i = pos - 1; i >= 0; --i) {
		if ((1 << i) & mask) {
			new_mask |= (1 << i);
		}
	}
	return new_mask;
}

void do_solve(const int mask, const int cnt, const int n) {
	if (cnt >= 2 * MN || dp[mask][cnt]) {
		return;
	}
	dp[mask][cnt] = 1;
	for (int pos = 0; pos < n; ++pos) {
		auto new_mask = do_flip(mask, pos, n);
		do_solve(new_mask, cnt + 1, n);
	}
}

int slow_solve(const std::string& str) {
	std::fill(&dp[0][0], &dp[(1 << MN) + 10][2 * MN + 10], 0);
	int mask = 0;
	int n = str.size();
	for (auto i = 0; i < n; ++i) {
		if (str[i] == '+') {
			mask |= (1 << (n - i - 1));
		}
	}
	do_solve(mask, 0, n);
	for (int i = 0; i <= 2 * n; ++i) {
		if (dp[(1 << n) - 1][i]) {
			return i;
		}
	}
	return -1;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	std::cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		std::string str;
		std::cin >> str;
		int ans = slow_solve(str);
		printf("Case #%d: %d\n", test, ans);
	}
}