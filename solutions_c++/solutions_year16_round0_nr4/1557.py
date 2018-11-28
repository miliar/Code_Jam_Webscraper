#pragma comment(linker, "/STACK:36777216")
#define _USE_MATH_DEFINES
#include <iostream>
#include <utility>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <climits>
#include <cstring>
#include <cmath>
#include <queue>
#include <functional>
#include <cstdio>
#include <cassert>
#include <stack>

#define mp make_pair
#define mt(x,y,z) mp((x), mp((y), (z)))
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;

// globals starts here

struct FractilesSolution
{
	int k, c, s;

	FractilesSolution(int _k, int _c, int _s)
	{
		k = _k;
		c = _c;
		s = _s;
	}

	void solve()
	{
		for (int i = 1; i <= k; ++i)
		{
			cout << i << " ";
		}
		cout << endl;
	}
};

int main()
{
#ifdef DEBUGAGA
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#elif defined(CONTEST)
	freopen(CONTEST ".in", "r", stdin);
	freopen(CONTEST ".out", "w", stdout);
#endif

	cin.sync_with_stdio(false);
	int tests;
	cin >> tests;

	for (int tc = 1; tc <= tests; ++tc)
	{
		cout << "Case #" << tc << ": ";
		int k, c, s;
		cin >> k >> c >> s;

		FractilesSolution sol(k, c, s);
		sol.solve();
	}

	return 0;
}