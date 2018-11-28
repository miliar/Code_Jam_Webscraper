#include <cstdio>
#include <iostream>
#include <vector>

int n, m;

void solve(void) {
	std::cin >> n >> m;
	for (long long string = 0; string < (1LL << n) && m > 0; string++) {
		if ((~string >> n - 1 & 1) || (~string & 1)) {
			continue;
		}
		std::vector<long long> factors;
		for (int base = 2; base <= 10; ++base) {
			long long number = 0, multiple = 1;
			for (int i = 0; i < n; ++i) {
				number += multiple * (string >> i & 1);
				multiple *= base;
			}
			bool prime = true;
			for (long long i = 2; i * i <= number; ++i) {
				if (number % i == 0) {
					factors.push_back(i);
					prime = false;
					break;
				}
			}
			if (prime) {
				break;
			}
		}
		if ((int)factors.size() == 9) {
			m--;
			for (int i = n - 1; i >= 0; --i) {
				std::cout << (string >> i & 1);
			}
			for (int i = 0; i < (int)factors.size(); ++i) {
				std::cout << " " << factors[i];
			}
			std::cout << std::endl;
		}
	}
}

int main(void) {
	int tests;
	std::cin >> tests;
	for (int i = 1; i <= tests; ++i) {
		std::cout << "Case #" << i << ":" << std::endl;
		solve();
	}
}