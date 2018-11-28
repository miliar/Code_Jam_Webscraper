#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <queue>
#include <complex>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(s) int((s).size())
#define len(s) int((s).size())
#ifdef LOCAL
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...) 42
#endif
#if _WIN32 || __WIN32__
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif
#define next _next
#define prev _prev
#define rank _rank
#define hash _hash
#define y0 yy0
#define y1 yy1
#define link _link

typedef long long ll;
typedef long long llong;
typedef long long int64;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef unsigned long long ullong;
typedef unsigned long long lint;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;

const int inf = int(1e9);
const double eps = 1e-9;
const double pi = 4 * atan(double(1));
const int N = 2020;

struct rect {
	
	int x1, y1, x2, y2;
	
	rect() {}
	
	rect(int x1, int y1, int x2, int y2) {
		this->x1 = x1;
		this->y1 = y1;
		this->x2 = x2;
		this->y2 = y2;
	}
	
};

struct point {

	int x, y;
	
	point() {}
	
	point(int x, int y) {
		this->x = x;
		this->y = y;
	}
	
};

bool used[N];
int d[N];
rect p[N];
int g[N][N];
point p1[10], p2[10];

inline int dist(point &a, point &b) {
	return max(abs(a.x - b.x), abs(a.y - b.y));
}

inline bool cross(int l1, int r1, int l2, int r2) {
	return max(l1, l2) <= min(r1, r2);
}

inline bool inSeg(int x, int l, int r) {
	return l <= x && x <= r;
}

inline int calc(rect &a, rect &b) {
	p1[0] = point(a.x1, a.y1);
	p1[1] = point(a.x1, a.y2);
	p1[2] = point(a.x2, a.y1);
	p1[3] = point(a.x2, a.y2);
	
	p2[0] = point(b.x1, b.y1);
	p2[1] = point(b.x1, b.y2);
	p2[2] = point(b.x2, b.y1);
	p2[3] = point(b.x2, b.y2);
	
	int ans = inf;
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			ans = min(ans, dist(p1[i], p2[j]));
		}
	}
	
	for (int i = 0; i < 4; ++i) {
		if (inSeg(p1[i].y, b.y1, b.y2)) {
			ans = min(ans, abs(p1[i].x - b.x1));
			ans = min(ans, abs(p1[i].x - b.x2));
		}
		if (inSeg(p1[i].x, b.x1, b.x2)) {
			ans = min(ans, abs(p1[i].y - b.y1));
			ans = min(ans, abs(p1[i].y - b.y2));
		}
	}
	
	for (int i = 0; i < 4; ++i) {
		if (inSeg(p2[i].y, a.y1, a.y2)) {
			ans = min(ans, abs(p2[i].x - a.x1));
			ans = min(ans, abs(p2[i].x - a.x2));
		}
		if (inSeg(p2[i].x, a.x1, a.x2)) {
			ans = min(ans, abs(p2[i].y - a.y1));
			ans = min(ans, abs(p2[i].y - a.y2));
		}
	}
	
	return ans;
}	

inline void solve() {
	int w, h, b;
	scanf("%d %d %d", &w, &h, &b);
	for (int i = 0; i < b; ++i) {
		scanf("%d %d %d %d", &p[i].x1, &p[i].y1, &p[i].x2, &p[i].y2);
		++p[i].x2;
		++p[i].y2;
	}
	p[b++] = rect(-100, 0, 0, h);
	p[b++] = rect(w, 0, w + 100, h);
	for (int i = 0; i < b; ++i) {
		for (int j = 0; j < b; ++j) {
			g[i][j] = calc(p[i], p[j]);
		}
		g[i][i] = 0;
	}
	for (int i = 0; i < b; ++i) {
		d[i] = inf;
		used[i] = false;
	}
	d[b - 2] = 0;
	for (int i = 0; i < b; ++i) {
		int best = -1;
		for (int j = 0; j < b; ++j) {
			if (!used[j] && (best == -1 || d[j] < d[best])) {
				best = j;
			}
		}
		used[best] = true;
		for (int j = 0; j < b; ++j) {
			d[j] = min(d[j], d[best] + g[best][j]);
		}
	}
	printf("%d\n", d[b - 1]);
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
