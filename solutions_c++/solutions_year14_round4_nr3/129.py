#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const int N = 1000 + 10;
const int INF = 1000000000;

struct Square
{
	int l, r, u, d;
	
	int distTo(const Square &b)
	{
		int dx, dy;
		if ((l <= b.l && b.l <= r) || (l <= b.r && b.r <= r)) dx = 0;
		else
			if (b.l > r) dx = b.l - r - 1;
			else dx = l - b.r - 1;
		if ((d <= b.d && b.d <= u) || (d <= b.u && b.u <= u)) dy = 0;
		else
			if (b.d > u) dy = b.d - u - 1;
			else dy = d - b.u - 1;
		return max(dx, dy);
	}
} a[N];
int dist[N][N], dst[N], vis[N];
int n, m, b;
int testCases;

void dijkstra()
{
	memset(vis, 0, sizeof vis);
	for (int i = 1; i <= b; ++i) dst[i] = INF;
	for (int t = 1; t <= b; ++t) {
		int k = -1;
		for (int i = 0; i <= b; ++i)
			if (! vis[i] && (k == -1 || dst[i] < dst[k])) k = i;
		vis[k] = 1;
		for (int i = 0; i <= b; ++i) dst[i] = min(dst[i], dst[k] + dist[k][i]);
	}
}

int main()
{
	cin >> testCases;
	for (int t = 1; t <= testCases; ++t) {
		cin >> n >> m >> b;
		for (int i = 1; i <= b; ++i) cin >> a[i].l >> a[i].d >> a[i].r >> a[i].u;
		a[0].l = -1;
		a[0].r = -1;
		a[0].d = 0;
		a[0].u = m - 1;
		++b;
		a[b].l = n;
		a[b].r = n;
		a[b].d = 0;
		a[b].u = m - 1;
		
		for (int i = 0; i <= b; ++i)
			for (int j = 0; j <= b; ++j) {
				if (i == j) continue;
				dist[i][j] = a[i].distTo(a[j]);
			}
					
		dijkstra();
		printf("Case #%d: %d\n", t, dst[b]);
	}
	return 0;
}
