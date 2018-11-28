#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <cstring>
#include <queue>
#include <deque>
#include <functional>
#include <climits>
#include <cassert>
#include <list>

#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))
#define ABS(a) (((a) > 0) ? (a) : (-(a)))
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))

using namespace std;
typedef long long ll;

int dx[] = { 0, 0, -1, 1 };
int dy[] = { -1, 1, 0, 0 };

char w[] = { '^', '<', '>', 'v' };

int get_dir(char c)
{
	if (c == '<')
		return 0;
	if (c == '>')
		return 1;
	if (c == '^')
		return 2;
	return 3;
}

int r, c;
vector<string> s;

bool exists(pair<int, int> e)
{
	if (e.first < 0 || e.second < 0 || e.first >= r || e.second >= c) return 0;
	return 1;
}

bool isok(int i, int j)
{
	int d = get_dir(s[i][j]);
	for (int k = 1; 1; k++)
	{
		pair<int, int> next = mp(i + dx[d] * k, j + dy[d] * k);
		if (!exists(next)) return 0;
		if (s[next.first][next.second] != '.') return 1;
	}
}


int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int t;
	cin >> t;

	for (int q = 0; q < t; q++)
	{
		cin >> r >> c;

		s.clear();
		s.resize(r);

		for (int i = 0; i < r; i++)
			cin >> s[i];

		int ans = 0;
		for (int i = 0; i < r; i++)
		{
			for (int j = 0; j < c; j++)
			{
				if (s[i][j] == '.') continue;
				if (isok(i, j)) continue;
				bool ok = 0;
				for (int k = 0; k < 4; k++)
				{
					s[i][j] = w[k];
					if (isok(i, j))
					{
						ok = 1;
						break;
					}
				}
				if (!ok)
				{
					printf("Case #%d: IMPOSSIBLE\n", q + 1);
					goto next_step;
				}
				ans++;
			}
		}
		printf("Case #%d: %d\n", q + 1, ans);
	next_step:;
	}

	return 0;
}