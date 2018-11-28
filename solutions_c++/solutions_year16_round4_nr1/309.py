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

using namespace std;
typedef long long ll;
typedef long double ld;
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))

const int N = 15;

char t[] = { 'P', 'R', 'S' };

string dp[N][3];

pair<int, int> g[3];

string f(int n, int c)
{
	if (n == 0)
	{
		return string() + t[c];
	}
	if (dp[n][c] != "*") return dp[n][c];
	
	string a = f(n - 1, g[c].first);
	string b = f(n - 1, g[c].second);

	if (a == b)
	{
		return dp[n][c] = "-";
	}

	return dp[n][c] = min(a + b, b + a);
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < 3; j++)
			dp[i][j] = "*";
	}

	g[0] = mp(0, 1);
	g[1] = mp(1, 2);
	g[2] = mp(0, 2);

	int tests;
	cin >> tests;
	for (int q = 0; q < tests; q++)
	{
		int n;
		cin >> n;
		int r, p, c;
		cin >> r >> p >> c;
		string ans = "-";
		for (int i = 0; i < 3; i++)
		{
			string cur = f(n, i);
			int rr = 0, pp = 0, cc = 0;
			for (int j = 0; j < cur.size(); j++)
			{
				if (cur[j] == 'R') rr++;
				if (cur[j] == 'P') pp++;
				if (cur[j] == 'S') cc++;
			}
			if (rr != r || cc != c || pp != p) continue;
			if (ans == "-") ans = cur;
			else if (cur < ans) ans = cur;
		}
		printf("Case #%d: ", q + 1);
		if (ans == "-") printf("IMPOSSIBLE\n");
		else cout << ans << endl;
	}

	return 0;
}