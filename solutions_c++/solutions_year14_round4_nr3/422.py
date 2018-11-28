#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cassert>

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <cfloat>
#include <unordered_map>

using namespace std;

typedef long long ll;
typedef long long li;
typedef unsigned int uint;
typedef unsigned long long ull;

#define y1 botva
void Solution(int test);

int main()
{
#ifdef DEBUG
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#else
#endif
	int ts; scanf("%d", &ts);
	for (int i = 1; i <= ts; i++)
		Solution(i);
	return 0;
}

bool all[110][510];

const int dx[4] = { 1, 0, -1, 0 };
const int dy[4] = { 0, 1, 0, -1 };
const int MAXE = 1000000;
const int MAXV = 200000;
int w, h, n, S, T;

int nx[MAXE], cap[MAXE], flow[MAXE], dest[MAXE], head[MAXV], fr, tag[MAXV], tg;

void add(int u, int v, int cp)
{
	nx[fr] = head[u];
	cap[fr] = cp, flow[fr] = 0;
	dest[fr] = v; head[u] = fr++;
}

void added(int u, int v, int cp)
{
	add(u, v, cp);
	add(v, u, 0);
}

bool dfs(int x)
{
	tag[x] = tg;
	if (x == T) {  return true;
	}
	for (int j = head[x]; j != -1; j = nx[j])
	{
		int v = dest[j];
		if (tag[v] == tg || flow[j] == cap[j]) continue;
		if (dfs(v))
		{
			flow[j]++; flow[j ^ 1]--;
			return true;
		}
	}
	return false;
}

void Solution(int test)
{
	fr = 0;
	fill(nx, nx + MAXE, -1);
	fill(head, head + MAXV, -1);
	scanf("%d%d%d", &w, &h, &n);
	for (int i = 0; i < w; i++)
		for (int j = 0; j < h; j++)
			all[i][j] = true;
	for (int i = 0; i < n; i++)
	{
		int xl, yl, xr, yr;
		scanf("%d%d%d%d", &xl, &yl, &xr, &yr);
		for (int j = xl; j <= xr; j++)
			for (int k = yl; k <= yr; k++)
				all[j][k] = false;
	}
	for (int i = 0; i < w; i++)
		for (int j = 0; j < h; j++)
		{
			if (!all[i][j]) continue;
			for (int k = 0; k < 4; k++)
			{
				int nx = i + dx[k], ny = j + dy[k];
				if (nx < 0 || nx >= w || ny < 0 || ny >= h) continue;
				if (!all[nx][ny]) continue;
				added(2 * (i * h + j) + 1, 2 * (nx * h + ny), 1);
				added(2 * (nx * h + ny) + 1, 2 * (i * h + j), 1);
			}
		}
	for (int i = 0; i < w; i++)
	{
		if (all[i][0])
			added(2 * w * h + 1, 2 * i * h, 1);
		if (all[i][h - 1])
			added(2 * (i * h + h - 1) + 1, 2 * (w * h + 1), 1);
	}
	for (int i = 0; i < w; i++)
		for (int j = 0; j < h; j++)
			if (all[i][j])
				added(2 * (i * h + j), 2 * (i * h + j) + 1, 1);
	S = 2 * w * h + 1, T = 2 * (w * h + 1);
	int ans = 0; tg = 1;
	fill(tag, tag + MAXV, 0);
	while (dfs(S)) tg++, ans++;
	printf("Case #%d: %d\n", test, ans);
}
