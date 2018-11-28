#pragma comment (linker, "/STACK:64000000")
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))

using namespace std;

#define maxw  105
#define maxh  505
const int maxn = 2 * maxw * maxh;
const int maxe = 8 * maxn;

bool used[maxw][maxh];
int w, h, b;
vector<int> e[maxn];
int c[maxe];
int tgt[maxe];
int src, n, sink;
int f[maxe];
int m;

int ver(int x, int y, int q) { return q * w * h + y * w + x; }

void add(int u, int v)
{
	c[m] = 1;
	c[m+1] = 0;
	tgt[m] = v;
	tgt[m+1] = u;
	e[u].push_back(m);
	e[v].push_back(m+1);
	m+=2;
}

int di[] = {-1, 1, 0, 0};
int dj[] = {0, 0, -1, 1};

bool dfs(int v)
{
	f[v] = true;
	if (v == sink) return true;
	for (auto &t : e[v]) if (!f[tgt[t]] && c[t])
	{
		if (dfs(tgt[t]))
		{
			c[t]--;
			c[t^1]++;
			return true;
		}
	}
	return false;
}

void solvecase() {
	scanf("%d%d%d", &w, &h, &b);
	FOR(i, w) FOR(j, h) used[i][j] = false;
	FOR(t, b)
	{
		int x0, y0, x1, y1;
		scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
		for (int x = x0; x <= x1; x++)
			for (int y = y0; y <= y1; y++)
				used[x][y] = true;
	}
	n = 2 * w * h + 2;
	src = n - 2;
	sink = n - 1;

	m = 0;
	FOR(i, n) e[i].clear();

	FOR(i, w) {
		add(src, ver(i, 0, 0));
		add(ver(i, h-1, 1), sink);
	}
	FOR(i, w) FOR(j, h) if (!used[i][j]) {
		add(ver(i, j, 0), ver(i, j, 1));
		FOR(d, 4)
		{
			int ii = i + di[d];
			int jj = j + dj[d];
			if (ii < 0 || jj < 0 || ii >= w || jj >= h) continue;
			add(ver(i, j, 1), ver(ii, jj, 0));
		}
	}
	int res = 0;
	while (true)
	{
		FOR(i, n) f[i] = false;
		if (dfs(src)) res++; else break;
	}
	printf("%d", res);
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main(int argc, const char **argv) {
	string fin = "input.txt", fout = "output.txt";
	if (argc > 1)
	{
		fin = argv[1];
		fout = fin + ".out";
	}
	freopen(fin.c_str(), "rt", stdin);
	freopen(fout.c_str(), "wt", stdout);
	solve();
	return 0;
}
