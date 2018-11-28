#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

std::string to_string(long long n, int base) {
	std::string ans;
	do {
		ans.push_back(n % base + '0');
		n /= base;
	} while (n);
	std::reverse(ans.begin(), ans.end());
	return ans;
}

long long mask_to_int(long long mask, int base, int n) {
	long long mul = 1;
	long long ans = 0;
	for (int i = 0; i <= n; ++i) {
		if ((1ll << i) & mask) {
			ans += mul;
		}
		mul *= base;
	}
	return ans;
}

long long get_divisor(long long n) {
	for (long long i = 2; i * i <= n; ++i) {
		if (n % i == 0) {
			return i;
		}
	}
	return -1;
}

void slow_solve(int n, int max) {
	long long iter = 1ll << (n - 2);
	int count = 0;
	while (count < max) {
		auto current = (iter << 1ll) | 1;
		bool ok = true;
		std::vector<long long> divisors;
		for (int base = 2; base <= 10; ++base) {
			auto divisor = get_divisor(mask_to_int(current, base, n));
			if (divisor != -1) {
				divisors.push_back(divisor);
			}
			else {
				break;
			}
		}
		if (divisors.size() == 9) {
			++count;
			std::cout << to_string(current, 2) << " ";
			for (const auto& divisor : divisors) {
				std::cout << divisor << " ";
			}
			std::cout << std::endl;
		}
		++iter;
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	std::cerr << mask_to_int(55, 3, 6) << std::endl;
	int tests;
	std::cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		int n, j;
		std::cin >> n >> j;
		printf("Case #%d:\n", test);
		slow_solve(n, j);
	}
}