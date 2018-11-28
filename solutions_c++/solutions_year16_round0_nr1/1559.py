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

void solve(ll n)
{
	if (n == 0)
	{
		cout << "INSOMNIA" << endl;
		return;
	}

	vector<bool> saw(10, false);

	ll mult = 0;
	
	while (true)
	{
		bool getout = true;
		for (int i = 0; i < 10; ++i)
		{
			if (!saw[i])
			{
				getout = false;
				break;
			}
		}

		if (getout)
		{
			break;
		}

		++mult;
		ll x = mult * n;

		while (x > 0)
		{
			saw[x % 10] = true;
			x /= 10;
		}
	}

	cout << mult * n << endl;
}

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
		ll n;
		cin >> n;

		solve(n);
	}

	return 0;
}