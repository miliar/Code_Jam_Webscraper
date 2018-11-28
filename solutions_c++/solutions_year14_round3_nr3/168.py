#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <string>
#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <queue>
#include <memory.h>
#include <cmath>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define fore(i, b, e) for (int i = (int)b; i <= (int)e; i++)
#define all(x) (x).begin(), (x).end()
#define se second
#define fi first
#define mp make_pair
#define pb push_back
#define op operator
typedef vector <int> vi;
typedef pair<int, int> pii;
typedef long long i64;

const int dx[4] = {-1, 1, 0, 0};
const int dy[4] = {0, 0, 1, -1};

const int maxn = 25;

bool empty[maxn][maxn];
bool vis[maxn][maxn];
int to_add, n, m;

bool dfs(int curx, int cury)
{
	if (curx <= 0 || curx > n || cury <= 0 || cury > m)
		return true;
	vis[curx][cury] = true;
	to_add++;
	bool ret = false;
	forn(move, 4)
	{
		int nnewx = curx + dx[move];
		int nnewy = cury + dy[move];
		if ((!vis[nnewx][nnewy]) && empty[nnewx][nnewy])
		{
			bool tmp = dfs(nnewx, nnewy);
			if (tmp)
				ret = true;
		}
	}
	return ret;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	fore(test, 1, tests)
	{
		printf("Case #%d: ", test);
		int K;
		scanf("%d%d%d", &n, &m, &K);
		int sz = n * m;
		int best = K;
		fore(prof, 0, (1 << sz) - 1)
		{
			int nnew = 0;
			forn(j, sz)
				if (prof & (1 << j))
					nnew++;
			if (nnew >= best)
				continue;
			int cur = 0;
			//printf("prof = %d\n", prof);
			fore(i, 1, n)
			{
				fore(j, 1, m)
				{
					empty[i][j] = ((prof & (1 << cur)) == 0);
					cur++;
				//	printf("%d", empty[i][j]);
				}
				//printf("\n");
			}
			fore(i, 0, n + 1)
				fore(j, 0, m + 1)
					vis[i][j] = false;
			fore(i, 0, n + 1)
				empty[i][0] = empty[i][m + 1] = true;
			fore(j, 0, m + 1)
				empty[0][j] = empty[n + 1][j] = true;
			int enclosed = nnew;
			fore(i, 1, n)
				fore(j, 1, m) if ((!vis[i][j]) && (empty[i][j]))
				{
					to_add = 0;
					bool f = dfs(i, j);
					if (!f)
						enclosed += to_add;
				}
			if (enclosed >= K)
				best = nnew;
		}
		printf("%d\n", best);
	}

	return 0;
}