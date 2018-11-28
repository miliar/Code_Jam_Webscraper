#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#define foreach(e,x) for(__typeof(x.begin()) e=x.begin(); e!=x.end(); ++e)

const int N = 2000 + 10;
const int dx[] = {0, 1, 0, -1};
const int dy[] = {-1, 0, 1, 0};

int w, h, n, tot, last;
int l[N], r[N], u[N], d[N];
int x[N];
int vis[N][N];

int dfs(int x, int y, int d)
{
	if (x < 0 || x >= h) return false;
	if (y < 0 || y >= w) return false;
	if (vis[x][y]) return 0;
	vis[x][y] = true;
	if (x == h - 1) return 1;
	for(int nd = d - 1; nd <= d + 1; ++ nd) {
		int md = (nd + 4) % 4;
		if (dfs(x + dx[md], y + dy[md], md))
			return true;
	}
	return false;
}

void solve(int test)
{
	printf("Case #%d: ", test);
	cin >> w >> h >> n;
	tot = 0;
	for(int i = 0; i < n; ++ i) {
		cin >> l[i] >> u[i];
		cin >> r[i] >> d[i];
		//x[tot ++] = u[i];
		//x[tot ++] = d[i] + 1;
	}
	/*
	for(int i = 0; i < h; ++ i) {
		x[tot ++] = 0;
	}
	x[tot ++] = 0;
	x[tot ++] = h;
	sort(x, x + tot);
	*/
	//tot = unique(x, x + tot) - x;
	//last = tot - 1;
	//for( ; x[last] >= h; -- last);
	memset(vis, 0, sizeof vis);
	for(int i = 0; i < n; ++ i) {
		//int s = lower_bound(x, x + tot, u[i]) - x;
		//int t = lower_bound(x, x + tot, d[i] + 1) - x;
		int s = u[i], t = d[i] + 1;
		for(int j = s; j < t; ++ j) {
			for(int k = l[i]; k <= r[i]; ++ k) {
				vis[j][k] = true;
			}
		}
	}
	int ret = 0;
	for(int i = 0; i < w; ++ i) {
		ret += dfs(0, i, 1);
	}
	cout << ret << endl;
}

int main()
{
	//freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);
	//freopen("C-small-attempt1.in", "r", stdin); freopen("C-small-attempt1.out", "w", stdout);
	//freopen("C-small-attempt2.in", "r", stdin); freopen("C-small-attempt2.out", "w", stdout);
	//freopen("C-small-attempt3.in", "r", stdin); freopen("C-small-attempt3.out", "w", stdout);
	freopen("C-small-attempt4.in", "r", stdin); freopen("C-small-attempt4.out", "w", stdout);
	//freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);
	int testcase;
	scanf("%d", &testcase);
	for(int i = 1; i <= testcase; ++ i) 
		solve(i);
	fclose(stdout);
	return 0;
}
