#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <numeric>
#include <string>
#include <cstring>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long int int64;

const int N = 150;

const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};

int r, c;
int mx[N][N];

bool in(int x, int y)
{
	return x >= 0 && x < r && y >= 0 && y < c;
}

void solve(int test)
{
	cin >> r >> c;
	for (int i = 0; i < r; i++)
	{
		string str;
		cin >> str;
		for (int j = 0; j < c; j++)
		{
			if (str[j] == '.')
				mx[i][j] = 4;
			if (str[j] == '^')
				mx[i][j] = 0;
			if (str[j] == '>')
				mx[i][j] = 1;
			if (str[j] == 'v')
				mx[i][j] = 2;
			if (str[j] == '<')
				mx[i][j] = 3;
		}
	}

	int ans = 0;

	for (int i = 0; i < r; i++)
	{
		for (int j = 0; j < c; j++)
		{
			if (mx[i][j] == 4)
				continue;
			
			vector<bool> good(4);

			for (int dir = 0; dir < 4; dir++)
			{
				int x = i + dx[dir];
				int y = j + dy[dir];

				while (true)
				{
					if (!in(x, y))
						break;
					if (mx[x][y] != 4)
					{
						good[dir] = true;
						break;
					}
					x += dx[dir];
					y += dy[dir];
				}
			}

			if (good[mx[i][j]])
				continue;
			
			bool any = false;

			for (int dir = 0; dir < 4; dir++)
			{
				if (!good[dir])
					continue;
				any = true;
				mx[i][j] = dir;
				ans++;
				break;
			}
			
			if (!any)
			{
				printf("Case #%d: IMPOSSIBLE\n", test);
				return;
			}
		}
	}

	printf("Case #%d: %d\n", test, ans);
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif

	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
		solve(i + 1);

	return 0;
}
