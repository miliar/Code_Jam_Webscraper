#include <cstdio>
#include <cmath>
#include <ctime>

#include <iostream>
#include <algorithm>
#include <string>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/math/special_functions/prime.hpp>
#include <boost/multiprecision/miller_rabin.hpp>

using boost::multiprecision::uint128_t;
using boost::math::prime;
using boost::math::max_prime;
using boost::multiprecision::miller_rabin_test;

boost::random::mt19937 gen;

uint128_t rebase(uint128_t n, int base)
{
	uint128_t res = 0;
	uint128_t acc = 1;

	while (n) {
		res += n % 2 == 1 ? acc : 0;
		n >>= 1;
		acc *= base;
	}

	return res;
}

uint128_t getdiv(uint128_t n)
{
	if (miller_rabin_test(n, 25, gen)) {
		return -1;
	}


	for (int i = 0; i < max_prime; i++) {
		if (n % prime(i) == 0) {
			return prime(i);
		}
	}

	return -1;
}

void printbin(uint128_t n, int digits)
{
	for (int i = digits - 1; i >= 0; i--) {
		std::cout.put(n & (1LL << i) ? '1': '0');
	}
}

uint128_t* testcoin(uint128_t coin)
{
	uint128_t* divs = new uint128_t[9];
	for (int i = 2; i <= 10; i++) {
		uint128_t b = rebase(coin, i);
		uint128_t div = getdiv(b);
		if (div == -1) {
			delete[] divs;
			divs = nullptr;
			break;
		} else {
			divs[i-2] = div;
		}
	}
	return divs;
}

int main()
{
	gen = boost::random::mt19937(clock());

	int c;
	std::cin >> c;
	for (int t = 1; t <= c; t++) {
		printf("Case #%d:\n", t);
		int length, count;
		std::cin >> length >> count;
		for (uint128_t i = 1; i < (1LL<<(length-1LL)) && count > 0; i += 2) {
			uint128_t num = i | (1LL<<(length-1LL));
			/* printf("Testing "); */
			/* printbin(num, length); */
			/* printf("\n"); */
			uint128_t* divs = testcoin(num);
			if (!divs) {
				continue;
			}
			printbin(num, length);
			for (int i = 0; i < 9; i++) {
				std::cout << ' ' << divs[i];
			}
			printf("\n");
			fflush(stdout);
			--count;
		}
		if (count > 0) {
			fprintf(stderr, "Something is amiss...\n");
		}
	}
}
