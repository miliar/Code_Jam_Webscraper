#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

void update(long long n, int& count, int& mask) {
	do {
		int digit = n % 10;
		if (!(mask & (1 << digit))) {
			++count;
			mask |= (1 << digit);
		}
		n /= 10;
	} while (n);
}

int slow_solve(long long n) {
	int mask = 0;
	int count = 0;
	int mul = 0;
	while (count != 10) {
		++mul;
		update(n * mul, count, mask);
	}
	return mul;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	std::cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		long long n;
		std::cin >> n;
		std::string ans = "INSOMNIA";
		if (n) {
			int mul = slow_solve(n);
			ans = std::to_string(n * mul);
		}
		printf("Case #%d: %s\n", test, ans.c_str());
	}
}