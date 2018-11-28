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

pair<string, string> solve(int n, int l, vector<string> g, string b)
{
	for (int i = 0; i < g.size(); ++i)
	{
		if (g[i] == b)
		{
			return mp("", "");
		}
	}

	string s1;
	for (int i = 0; i < l; ++i)
	{
		s1 += "0?";
	}

	string s2;
	for (int i = 0; i < l-1; ++i)
	{
		s2.push_back('1');
	}

	if (s2.size() == 0)
	{
		s2 = "0";
	}

	return mp(s1, s2);
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
		int n, l;
		cin >> n >> l;

		vector<string> g;
		for (int i = 0; i < n; ++i)
		{
			string s;
			cin >> s;
			g.push_back(s);
		}

		string b;
		cin >> b;

		auto ans = solve(n, l, g, b);
		if (ans.first.empty())
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << ans.first << " " << ans.second << endl;
		}
	}

	return 0;
}