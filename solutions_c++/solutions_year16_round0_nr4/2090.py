#include <cstdio>
#include <cmath>

#include <iostream>
#include <algorithm>
#include <vector>

#include <boost/multiprecision/integer.hpp>
#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::int1024_t;
using boost::multiprecision::uint1024_t;

int1024_t pow(int1024_t base, int1024_t exp)
{
	if (exp == 0) {
		return 1;
	}

	if (exp % 2 == 0) {
		int1024_t tmp = pow(base, exp >> 1);
		return tmp * tmp;
	} else {
		int1024_t tmp = pow(base, exp >> 1);
		return (tmp * tmp) * base;
	}
}

std::vector<int1024_t> solve(int1024_t k, int1024_t c, int1024_t s)
{
	if (k != s) {
		return std::vector<int1024_t>(0);
	}

	int1024_t kc1 = pow(k, c - 1);

	std::vector<int1024_t> sol;

	int1024_t tmp = 0;
	for (int i = 0; i < k; i++) {
		sol.push_back(tmp);
		tmp += kc1;
	}

	return sol;
}

int main()
{
	int c;
	std::cin >> c;
	for (int t = 1; t <= c; t++) {
		int k, c, s;
		std::cin >> k >> c >> s;
		std::cout << "Case #" << t << ":";
		std::vector<int1024_t> indexes = solve(k, c, s);
		if (indexes.empty()) {
			std::cout << " IMPOSSIBLE";
		} else {
			for (const int1024_t& i : indexes) {
				std::cout << ' ' << (i+1);
			}
		}
		std::cout << std::endl;
	}
}
