
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <unordered_map>
#include <unordered_set>
#include <memory>
using namespace std;

int n, m;
char s[128][128];

unordered_map<int,int> H;

int calc(const int mask)
{
	unordered_set<string> S;
	for (int i = 0; i < m; i++)
	{
		if (mask & (1<<i))
		{
			const int l = strlen(s[i]);
			for (int j = 0; j <= l; j++)
			{
				const char c = s[i][j];
				s[i][j] = '\0';
				S.insert(s[i]);
				s[i][j] = c;
			}
		}
	}
	return S.size();
}

void solve(int si, int mask, int r)
{
	if (si < n-1)
	{
		for (int sm = mask; sm; sm = (sm-1)&mask)
		{
			solve(si+1, mask & (~sm), r + calc(sm));
		}
	}
	else
	{
		r += calc(mask);

		auto h = H.find(r);
		if (h == H.end())
		{
			H[r] = 1;
		}
		else
		{
			h->second++;
		}
	}
}

int main()
{
	gets(s[0]);
	int test_cases;
	sscanf(s[0], "%d", &test_cases);

	for (int test_case = 1; test_case <= test_cases; test_case++)
	{
		gets(s[0]);
		sscanf(s[0], "%d %d", &m, &n);
		for (int i = 0; i < m; i++)
		{
			gets(s[i]);
		}

		H.clear();

		solve(0, (1<<m)-1, 0);

		int x = 0, y = 0;
		for (auto const& h : H)
		{
			if (h.first > x)
			{
				x = h.first;
				y = h.second;
			}
		}

		printf("Case #%d: %d %d\n", test_case, x, y);
	}

	return 0;
}