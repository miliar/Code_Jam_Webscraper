#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <map>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

int W, H;
int n;
struct Bldg {
	int x1, y1, x2, y2;
};

Bldg b[1001];

int g[1010][1010];
int w, h;
int SSRC, SSINK;

int flowBetween(Bldg a, Bldg b)
{
	int dx = 0, dy = 0;
	if (b.x1 > a.x2) dx = b.x1 - a.x2 - 1;
	if (a.x1 > b.x2) dx = a.x1 - b.x2 - 1;
	if (b.y1 > a.y2) dy = b.y1 - a.y2 - 1;
	if (a.y1 > b.y1) dy = a.y1 - b.y2 - 1;
	return max(dx, dy);
}


const int INF = 999666111;
int ds[10010], ps[10010], pr[10010];

void dijkstra(int root)
{
	for (int i = 0; i < n; i++) {
		ps[i] = 0; pr[i] = -1; ds[i] = INF;
	}
	ds[root] = 0;
	while (1) {
		int bi = -1, mdist = INF;
		for (int i = 0; i < n; i++) if (!ps[i] && ds[i] < mdist) {
			mdist = ds[i];
			bi = i;
		}
		if (bi == -1) return;
		ps[bi] = 1;
		for (int i = 0; i < n; i++) {
			int y = i;
			int ncost = ds[bi] + g[bi][i];
			if (!ps[y] && ds[y] > ncost) {
				pr[y] = bi;
				ds[y] = ncost;
			}
		}
	}
}

int solve(void)
{
	scanf("%d%d%d", &w, &h, &n);
	FOR(i, n) {
		scanf("%d%d%d%d", &b[i].x1, &b[i].y1, &b[i].x2, &b[i].y2);
	}
	FOR(i, 1010) FOR(j, 1010) g[i][j] = INF;
	if (n == 0) return w;
	
	FOR(i, n) FOR(j, n) if (j > i) {
		g[i][j] = g[j][i] = flowBetween(b[i], b[j]);
		//printf("g(%d, %d) = %d\n", i, j, g[i][j]);
	}
	n += 2;
	SSRC = n - 2;
	SSINK = n - 1;
	FOR(i, n - 2) {
		g[SSRC][i] = b[i].x1;
		g[i][SSINK] = w - 1 - b[i].x2;
	}
	g[SSRC][SSINK] = INF;
	dijkstra(SSRC);
	/*
	printf("best path len = %d\n", ds[SSINK]);
	printf("Backtrace: ");
	int x = SSINK;
	while (x != -1) {
		printf(" %d", x);
		x = pr[x];
		
	}
	printf("\n");
	*/
	return ds[SSINK];
}

int main(void)
{
#ifdef  DEBUG
	freopen("/home/vesko/gcj/C-small-attempt0.in", "rt", stdin);
#endif
	int nTests;
	scanf("%d", &nTests);
	FOR(tc, nTests) {
		printf("Case #%d: %d\n", tc + 1, solve());
	}
	return 0;
}

