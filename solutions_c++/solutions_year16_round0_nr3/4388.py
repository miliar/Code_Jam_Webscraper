#include <boost/range/irange.hpp>
#include <boost/format.hpp>
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;
using namespace boost;

typedef long long ll;
inline auto irange(int start, int end) { return boost::irange(start, end); }

ll get_num(const int& n, unordered_set<ll>& used)
{
	auto mod = 1 << (n - 1);
	ll value = (mod + rand() % mod) | 1;

	while (used.find(value) != used.end())
		value = (mod + rand() % mod) | 1;

	used.insert(value);
	return value;
}

ll change_base(ll num, const int& base)
{
	if (base == 2)
		return num;

	ll res = 0;
	ll mult = 1;

	while (num > 0)
	{
		res += (num & 1) * mult;
		num >>= 1;
		mult *= base;
	}

	return res;
}

bool add_div(const ll& num, vector<ll>& divs)
{
	for (ll d = 2; d * d <= num; d++)
		if (num % d == 0)
		{
			divs.push_back(d);
			return true;
		}

	return false;
}

string to_binary(ll num)
{
	string res = "";
	while (num)
	{
		res += (num & 1) + '0';
		num >>= 1;
	}

	reverse(res.begin(), res.end());
	return res;
}

int main()
{
	srand(time(NULL));
	
	int t;
	scanf("%d", &t);

	int n, j;
	scanf("%d %d", &n, &j);

	unordered_set<ll> used;
	vector<pair<ll, vector<ll>>> results;

	while ((int)results.size() < j)
	{	
		auto num = get_num(n, used);
		vector<ll> divs;

		for (ll base : irange(2, 11))
			if (!add_div(change_base(num, base), divs))
				break;
		
		// printf("divs size: %d\n", (int)divs.size());

		if (divs.size() == 9)
			results.push_back({num, divs});
	}

	puts("Case #1:");
	for (auto res : results)
	{
		printf("%s ", to_binary(res.first).c_str());
		for (auto num : res.second)
			printf("%lld ", num);

		puts("");
	}
}