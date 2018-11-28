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

int ans = 0;

string step(const string& s)
{
	string res;
	for (int i = 1; i <= s.size(); i++)
	{
		if (i == s.size())
		{
			res.push_back(s[i - 1]);
			break;
		}
		if (s[i] == s[i - 1])
		{
			i++;
			ans += 10;
		}
		else
		{
			res.push_back(s[i - 1]);
		}
	}
	return res;
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int te;
	cin >> te;
	for (int q = 0; q < te; q++)
	{
		ans = 0;
		string s;
		cin >> s;

		int prv = 0;
		while (1)
		{
			s = step(s);
			if (ans == prv) break;
			prv = ans;
		}

		printf("Case #%d: %d\n", q + 1, ans + s.size() / 2 * 5);

	}

	return 0;
}