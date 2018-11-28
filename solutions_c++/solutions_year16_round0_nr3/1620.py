#include <algorithm>
#include <array>
#include <chrono>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <deque>
#include <forward_list>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <regex>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <valarray>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

#define DIVISOR_TEST_MAX	10000

using namespace std;

typedef boost::multiprecision::int128_t BigInt;

class Number : public vector<char>
{
public:
	Number(size_t length) : vector<char>(length, 0)
	{ }

	void increase()
	{
		for (size_t i = 1; i < size(); i++)
		{
			char& b = (*this)[i];
			if (b)
				b = 0;
			else
			{
				b = 1;
				break;
			}
		}
	}

	BigInt toBase(BigInt base) const
	{
		BigInt val = 0;
		for_each(rbegin(), rend(), [base, &val](char x)
			{
				val *= base;
				val += x;
			});
		return val;
	}
};

class FindDivisor
{
public:
	const Number& nb;
	FindDivisor(const Number& nb) : nb(nb)
	{
	}

	BigInt operator()(int b) const
	{
		BigInt val = nb.toBase(b);
		BigInt maxD = min((BigInt)(sqrt((long double)val) + 0.5), (BigInt)DIVISOR_TEST_MAX);
		for (BigInt d = 2; d <= maxD; d++)
		{
			if (val % d == 0)
				return d;
		}
		return -1;
	}
};

vector<pair<Number, array<BigInt, 9>>> findJamcoins(int N, int J)
{
	vector<pair<Number, array<BigInt, 9>>> jamcoins;

	Number nb(N);
	nb[0] = 1;
	nb.back() = 1;

	array<int, 9> bases = { 2, 3, 4, 5, 6, 7, 8, 9, 10 };
	while (jamcoins.size() < J)
	{
		array<BigInt, 9> divisors;
		transform(bases.begin(), bases.end(), divisors.begin(), FindDivisor(nb));

		if (all_of(divisors.begin(), divisors.end(),
			[](auto d)
			{
				return d > 0;
			}))
		{
			jamcoins.emplace_back(nb, divisors);

			for_each(nb.rbegin(), nb.rend(),
				[](char b)
				{
					cout << (b ? '1' : '0');
				});

			for (auto d : divisors)
				cout << ' ' << d;
			cout << endl;
		}

		nb.increase();
	}

	return jamcoins;
}

int main()
{
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int N, J;
		cin >> N >> J;

		cout << "Case #" << t + 1 << ':' << endl;
		auto jamcoins = findJamcoins(N, J);
#if 0
		for (const auto& jamcoin : jamcoins)
		{
			for_each(jamcoin.first.rbegin(), jamcoin.first.rend(),
				[](char b)
				{
					cout << (b ? '1' : '0');
				});

			for (int d : jamcoin.second)
				cout << ' ' << d;
			cout << endl;
		}
#endif
	}

	return 0;
}
