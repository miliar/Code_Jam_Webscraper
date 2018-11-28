#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <set>
#include <map>
#include <math.h>
#include <cassert>
#include <cxxptl.h>
#include <sys/time.h>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

char a[102][102];
int b[102][102];
int by[102][2], bx[102][2];

enum {
	TOP = 1,
	BOTTOM = 2,
	LEFT = 4,
	RIGHT = 8,
};

int solve(void)
{
	int r, c;
	scanf("%d%d", &r, &c);
	FOR(i, r) scanf("%s", a[i]);
	
	memset(b, 0, sizeof(b));
	FOR(y, r) {
		int x;
		for (x = 0; x < c; x++) if (a[y][x] != '.') break;
		if (x < c) b[y][x] |= LEFT;
		by[y][0] = x;
		for (x = c - 1; x >= 0; x--) if (a[y][x] != '.') break;
		if (x >= 0) b[y][x] |= RIGHT;
		by[y][1] = x;
		
	}
	FOR(x, c) {
		int y;
		for (y = 0; y < r; y++) if (a[y][x] != '.') break;
		if (y < r) b[y][x] |= TOP;
		bx[x][0] = y;
		for (y = r - 1; y >= 0; y--) if (a[y][x] != '.') break;
		if (y >= 0) b[y][x] |= BOTTOM;
		bx[x][1] = y;
	}
	int cost = 0;
	FOR(y, r) FOR(x, c) {
		int mask = b[y][x];
		if (!mask) continue;
		if (mask == 15) return -1;
		int minPrice = 1;
		if ((mask & TOP) && !(mask & BOTTOM) && a[y][x] == 'v') minPrice = 0;
		if (!(mask & TOP) && (mask & BOTTOM) && a[y][x] == '^') minPrice = 0;
		if ((mask & LEFT) && !(mask & RIGHT) && a[y][x] == '>') minPrice = 0;
		if (!(mask & LEFT) && (mask & RIGHT) && a[y][x] == '<') minPrice = 0;
		
		if ((a[y][x] == '<' || a[y][x] == '>') && by[y][0] < x && x < by[y][1]) minPrice = 0;
		if ((a[y][x] == '^' || a[y][x] == 'v') && bx[x][0] < y && y < bx[x][1]) minPrice = 0;
		cost += minPrice;
	}
	return cost;
}

int main(int argc, char** argv)
{
#ifdef __LOCAL__
	freopen("/home/vesko/gcj/a.in", "rt", stdin);
#endif
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int res = solve();
		if (res >= 0)
			printf("Case #%d: %d\n", tc, res );
		else
			printf("Case #%d: IMPOSSIBLE\n", tc);
	}
	return 0;
}
