#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <utility>
#include <ctime>
#include <string>
#include <sstream>
#include <queue>
#include <cstring>
#include <functional>
#include <stack>

using namespace std;
typedef long long ll;
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))

// template end

ll points(const string& s)
{
	stack<char> sets;
	int pts = 0;
	for (int i = 0; i < s.size(); ++i)
	{
		if (sets.empty())
		{
			sets.push(s[i]);
			continue;
		}

		if (sets.top() == s[i])
		{
			sets.pop();
			pts += 10;
			continue;
		}

		int rest = s.size() - i;
		if (rest > sets.size())
		{
			sets.push(s[i]);
		}
		else
		{
			sets.pop();
			pts += 5;
		}
	}

	return pts;
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#elif defined CONTEST
	freopen(CONTEST".in", "r", stdin);
	freopen(CONTEST".out", "w", stdout);
#endif

	//ios_base::sync_with_stdio(false);
	
	int tests;
	cin >> tests;
	
	for (int tc = 1; tc <= tests; ++tc)
	{
		printf("Case #%d: ", tc);
		string s;
		cin >> s;

		ll ans = points(s);
		cout << ans << endl;
	}

	return 0;
}