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

struct PancakeSolution
{
	string str;

	PancakeSolution(const string& _str)
	{
		str = _str;
	}

	int makeprefix(int len, char target)
	{
		int pos = len - 1;

		for (; pos >= 0; --pos)
		{
			if (str[pos] != target)
			{
				break;
			}
		}

		if (pos < 0)
		{
			return 0;
		}

		return makeprefix(pos + 1, target == '+' ? '-' : '+') + 1;
	}

	void dosolve()
	{
		int ans = makeprefix(str.length(), '+');
		cout << ans << endl;
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
		string str;
		cin >> str;

		PancakeSolution sol(str);
		sol.dosolve();
	}

	return 0;
}