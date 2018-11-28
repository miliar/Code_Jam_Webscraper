#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>
#include <set>
#include <cstring>
#include <map>

using namespace std;

#define forsn(i, s, n) for (int i = s; i < n; i++)
#define forn(i, n) forsn(i, 0, n)
#define fore(i, n) forn(i, n.size())
#define all(n) n.begin(), n.end()

const map <char, string> nextR = {
	{'R', "RS"},
	{'P', "PR"},
	{'S', "SP"}
};

string go(int n, char c)
{
	if (n == 0)
		return string(1, c);
	
	string left = go(n - 1, nextR.at(c)[0]);
	string right = go(n - 1, nextR.at(c)[1]);

	return min(left + right, right + left);
}

string solve(int n, int r, int p, int s)
{
	string res = "Z";

	for (auto &k : nextR)
	{
		string sol = go(n, k.first);
		if (count(all(sol), 'R') == r && count(all(sol), 'P') == p && count(all(sol), 'S') == s)
			res = min(res, sol);
	}

	if (res == "Z")
		return "IMPOSSIBLE";
	
	return res;
}

int main()
{
	int t; cin >> t;

	forsn(z, 1, t + 1)
	{
		int n, r, p, s;
		cin >> n >> r >> p >> s;

		printf("Case #%d: %s\n", z, solve(n, r, p, s).c_str());
	}

	return 0;
}
