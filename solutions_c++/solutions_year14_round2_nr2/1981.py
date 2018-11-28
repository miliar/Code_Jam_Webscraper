#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <iterator>
#include <list>
#include <set>
#include <queue>
#include <numeric>
#include <cstdlib>
#include <ctime>
#include <limits>

using namespace std;

typedef long long lli;
typedef long li;

template <class T>
T Maximize (T &v, T nv) { if (nv > v) v = nv; return v; }

template <class T>
T Minimize (T &v, T nv) { if (nv < v) v = nv; return v; }

const lli INFLL = numeric_limits<lli>::max();
const li INF = numeric_limits<li>::max();

void solve ()
{
	ios::sync_with_stdio(0);

	li tests;
	cin >> tests;

	for (li test = 1; test <= tests; ++ test)
	{
		li A, B, K;
		cin >> A >> B >> K;

		li res = 0;
		for (li a = 0; a < A; ++ a)
		{
			for (li b = 0; b < B; ++ b)
			{
				res += (a & b) < K;
			}
		}

		cout << "Case #" << test << ": ";
		cout << res;
		cout << '\n';
	}
}

void init ()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

int main()
{
	init();
	solve();
	return 0;
}
