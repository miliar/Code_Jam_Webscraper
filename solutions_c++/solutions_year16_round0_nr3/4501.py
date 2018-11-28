#include <iostream>
#include <string>
#include <cstdlib>
#include <cmath>

void translateBase(const std::string &jamcoin, uint64_t values[9]) {
	for (int i = 2; i < 11; ++i)
		values[i - 2] = std::strtol(jamcoin.c_str(), nullptr, i);
}

void nextJamcoin(std::string &jamcoin) {
	*(jamcoin.end() - 2) += 1;
	for (int i = jamcoin.length() - 2; i > 1; --i) {
		if (jamcoin[i] <= '1')
			return;
		jamcoin[i - 1] += 1;
		jamcoin[i] = '0';
	}
	jamcoin[0] = '1';
}

void print_result(const std::string &jamcoin, uint64_t divisors[9]) {
	std::cout << jamcoin;
	for (int i = 0; i < 9; ++i)
		std::cout << " " << divisors[i];
	std::cout << std::endl;
}

bool findDivisors(const uint64_t values[9], uint64_t divisors[9]) {
	int found = 0;
	for (int i = 0; i < 9; ++i) {
		int value = std::sqrt(values[i]) + 1;
		for (int j = 2; j < value; ++j)
			if (values[i] % j == 0) {
				divisors[i] = j;
				found += 1;
				break;
			}
		if (found != i + 1)
			return false;
	}
	return found == 9;
}

void do_work(int n, int j) {
	std::string jamcoin = "1";
	for (int i = 0; i < n - 2; ++i)
		jamcoin += "0";
	jamcoin += "1";
	int found = 0;
	uint64_t values[9];
	uint64_t divisors[9];
	while (found < j) {
		translateBase(jamcoin, values);
		if (!findDivisors(values, divisors)) {
			nextJamcoin(jamcoin);
			continue;
		}
		found += 1;
		print_result(jamcoin, divisors);
		nextJamcoin(jamcoin);
	}
}

int main() {
	int t;
	std::cin >> t;
	for (int i = 1; i <= t; ++i) {
		int n, j;
		std::cin >> n >> j;
		std::cout << "Case #" << i << ":" << std::endl;
		do_work(n, j);
	}
	return 0;
}
