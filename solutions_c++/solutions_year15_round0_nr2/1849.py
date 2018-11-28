#include<iostream>
#include<cstdint>
#include<vector>
#include<set>
#include<algorithm>
#include <functional>
#include <iterator>

using namespace std;

uint64_t solve(multiset<uint64_t>& P)
{
	uint64_t maxc = *(P.rbegin());
	uint64_t value = maxc;

	for (uint64_t i = 1; i <= maxc; ++i)
	{
		uint64_t x = 0;
		auto ub = P.upper_bound(i);

		for (auto ubi = ub; ubi != P.end(); ++ubi)
		{
			x += ((*ubi - i) / i) + ((*ubi - i) % i == 0 ? 0 : 1);
		}
		value = min(value, i + x);
	}
	return value;
}

int main()
{
	uint64_t T;
	cin >> T;

	for (uint64_t t = 0; t < T; ++t)
	{
		uint64_t D;
		multiset<uint64_t> P;
		cin >> D;
		for (uint64_t i = 0; i < D; ++i)
		{
			uint64_t Pi;
			cin >> Pi;
			P.insert(Pi);
		}
		auto s = solve(P);

		cout << "Case #" << t + 1 << ": " << s << endl;
	}
	return 0;
}
