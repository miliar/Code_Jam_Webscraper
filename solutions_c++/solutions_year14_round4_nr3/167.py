#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <functional>
using namespace std;

typedef long long int64;
#define PB push_back
#define MP make_pair
#define debug(x) cout<<(#x)<<": "<<(x)<<endl
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)
#define MOD 1000000007

#define N 1010
struct point {
	int x, y;
} p0[N], p1[N];

const int inf = 1 << 28;
int e[N][N], dis[N];
bool vis[N];

int disPt(const point& A, const point& B) {
	return max(abs(A.x-B.x), abs(A.y-B.y)) - 1;
}

bool overlap(int a0, int a1, int b0, int b1) {
	if (a0 > b0) {
		swap(a0, b0);
		swap(a1, b1);
	}
	return (b0 <= a1);
}

int disRect(const point& A0, const point& A1, const point& B0, const point& B1) {
	point A, B;
	if (A0.x < B0.x) A.x = A1.x, B.x = B0.x;
	else A.x = A0.x, B.x = B1.x;
	if (A0.y < B0.y) A.y = A1.y, B.y = B0.y;
	else A.y = A0.y, B.y = B1.y;
	if (overlap(A0.x, A1.x, B0.x, B1.x)) return abs(A.y - B.y) - 1;
	if (overlap(A0.y, A1.y, B0.y, B1.y)) return abs(A.x - B.x) - 1;
	return disPt(A, B);
}

int shortestPath(int n, int s, int t) {
	REP(i, n) {
		dis[i] = inf;
		vis[i] = 0;
	}
	dis[s] = 0;
	REP(itr, n) {
		int minDis = inf, k = -1;
		REP(i, n) if (!vis[i] && dis[i] < minDis) {
			k = i;
			minDis = dis[i];
		}
		// printf("dis[%d] = %d\n", k, dis[k]);
		if (k == t) return minDis;
		vis[k] = 1;
		REP(i, n) dis[i] = min(dis[i], dis[k] + e[k][i]);
	}
	return -1;
}

int main() {
	int tN;
	cin >> tN;
	FOR(cN, 1, tN) {
		int W, H, n;
		cin >> W >> H >> n;
		int s = n, t = n+1;
		REP(i, n) cin >> p0[i].x >> p0[i].y >> p1[i].x >> p1[i].y;
		memset(e, 0, sizeof(e));
		e[s][t] = W;
		REP(i, n)
		FOR(j, i+1, n-1) e[i][j] = e[j][i] = disRect(p0[i], p1[i], p0[j], p1[j]);
		int i = 0, j = 1;
		REP(i, n) e[s][i] = p0[i].x;
		REP(i, n) e[i][t] = W-1 - p1[i].x;
		n += 2;
		/*
		REP(i, n) {
			REP(j, n) printf("%d ", e[i][j]);
			puts("");
		}
		*/
		int ans = shortestPath(n, s, t);
		printf("Case #%d: %d\n", cN, ans);
	}
}
