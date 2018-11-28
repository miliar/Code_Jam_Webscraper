#include <boost/range/irange.hpp>
#include <boost/format.hpp>
#include <cstdio>
#include <iostream>

using namespace std;
using namespace boost;

inline auto irange(int start, int end) { return boost::irange(start, end); }

int main()
{
	ios::sync_with_stdio(false);

	int t;
	cin >> t;

	for (int i : irange(1, t + 1))
	{
		string s;
		cin >> s;

		int res = 0;
		for (int pos : irange(1, s.size()))
			if (s[pos] != s[pos - 1])
				res++;

		cout << format("Case #%d: %d\n") % i % (res + (s.back() == '-'));
	}
}