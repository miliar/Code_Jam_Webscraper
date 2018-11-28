#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <cmath>

using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

const int DX[] = {0, 1, 0, -1};
const int DY[] = {1, 0, -1, 0};
const char DNAME[] = {'>', 'v', '<', '^'};
const int N = (int)1e3 + 10;
char table[N][N];
int n, m;

int getDir(char c)
{
	for (int i = 0; i < 4; i++)
		if (DNAME[i] == c)
			return i;
	throw;
}

bool checkPos(int x, int y)
{
	return x >= 0 && y >= 0 && x < n && y < m;
}

bool isSafeDir(int x, int y, int dir)
{
	while (1)
	{
		x += DX[dir];
		y += DY[dir];
		if (!checkPos(x, y))
			return false;
		if (table[x][y] != '.')
			return true;
	}
}

void solve()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++)
		scanf(" %s", table[i]);
	int moves = 0;
	for (int i = 0; i < n; i++)
	{
		for (int s = 0; s < m; s++)
		{
			if (table[i][s] == '.') continue;
			int id = getDir(table[i][s]);
		
			bool ok = false;
			for (int q = 0; q < 4; q++)
			{
				int d = (id + q) % 4;
				if (isSafeDir(i, s, d))
				{
					moves += (q == 0 ? 0 : 1);
					ok = true;
					break;
				}
			}
			if (!ok)
			{
				printf("IMPOSSIBLE\n");
				return;
			}
		}
	}
	printf("%d\n", moves);
}

int main()
{
	int t;	
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
