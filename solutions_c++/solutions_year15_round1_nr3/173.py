#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <memory.h>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PI;
typedef vector<PI> VPI;

#define FOR(i,a,n) for (int i = (a); i < (n); ++i)
#define FORE(i,a,n) for (int i = (a); i <= (n); ++i)
#define FORD(i,a,b) for (int i = (a); i >= (b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPE(i,n) FORE(i,0,n)
#define LL long long
#define FIR(n) REP(i,n)
#define FJR(n) REP(j,n)
#define ALL(v) v.begin(), v.end()

#define FI FIR(n)
#define FJ FJR(n)
#define FR(i,a) FOR(i,a,n)
#define REPN(i) REP(i,n)

#define GI(n) scanf("%d", &n)
#define GI2(n,m) scanf("%d %d", &n, &m)


// TYPES
template<class T> struct point_t {
	T x;
	T y;
	point_t(T x = T(), T y = T()) : x(x), y(y) {}

	bool operator<(const point_t<T>& p) const {
		return x == p.x ? y < p.y : x < p.x;
	}

	bool operator==(const point_t<T>& p) const {
		return x == p.x && y == p.y;
	}
};
typedef point_t<LL> point;


// UTILS
template<class T> point_t<T> operator+(point_t<T> p1, point_t<T> p2) {
	return point_t<T>(p1.x + p2.x, p1.y + p2.y);
}
template<class T> point_t<T> operator-(point_t<T> p1, point_t<T> p2) {
	return point_t<T>(p1.x - p2.x, p1.y - p2.y);
}

template<class T> T inline vp (point_t<T> p1, point_t<T> p2) {
	return p1.x*p2.y - p1.y*p2.x;
}

template<class T> T inline cp (point_t<T> p1, point_t<T> p2) {
	return p1.x*p2.x + p1.y*p2.y;
}

template<class T> T area_x2(point_t<T> p1, point_t<T> p2, point_t<T> p3) {
	return vp(p2 - p1, p3 - p1);
}

// in returned vector first and last vertexes are not the same
// returned in counter-clockwise order
vector<point> convex_hull_wrap(const vector<point>& vert) {
	size_t n = vert.size();
	point right = *max_element(ALL(vert)), left = *min_element(ALL(vert));

	vector<point> hull;

	point p = left;
	bool lower = true;
	do {
		hull.push_back(p);
		point best = lower ? right : left;
		FI if ( area_x2(p, vert[i], best) > 0 ) best = vert[i];
		p = best;
		if (best == right) lower = false;
	} while (! (p == left));

	return hull;
}

// first and last points in poly must be the same
// -1 inside, 0 on border, 1 outside
template<class T> int pt_inside(point_t<T> p, const vector< point_t<T> >& poly) {
	int cnt = 0;
	FOR(i, 1, poly.size()) {
		point_t<T> p1 = poly[i-1], p2 = poly[i];
		if (p1.y > p2.y) swap(p1, p2);
		if (p1.y<=p.y&&p.y<=p2.y) {
			T VP = area_x2(p, p1, p2);
			if (!VP) {
				if (p1.x<p2.x?p1.x<=p.x&&p.x<=p2.x:p2.x<=p.x&&p.x<=p1.x)
					return 0;
			} else 
				cnt += VP>0&&p1.y!=p.y;
		}
	}

	return (cnt & 1) ? -1 : 1;
}


int res[3010];
int n;
point p[3010];
point q[6010];

int bc(int n) {	int res =0; while (n) {n &= n-1; ++res;} return res;}


int half(const point p) {
	if (p.y > 0 || (p.y == 0 && p.x > 0))
		return 0;
	return 1;
}

int cmp(const point& p1, const point& p2) {
	int h1 = half(p1), h2 = half(p2);
	if (h1 != h2)
		return h1 < h2;
	LL x = vp(p1, p2);
	if (x) return x > 0;
	return p1 < p2;
		
}

void solve() {
	GI(n);
	int x, y;
	FI {
		GI2(x, y);
		p[i] = point(x, y);
	}
	if (n <=2) {
		FI res[i] = 0;
		return;
	}

	int N1 = n-1;
	FI {
		int pp=0;
		FJ if (i!=j )q[pp++] = p[j] - p[i];
		
		sort(q, q+N1, cmp);
		FOR(k, 0, N1) q[N1+k] = q[k];
		int j = 0;
		res[i] = 10000000;
		REP(k, N1) {
			while (j < k + N1 && vp(q[k], q[j]) >=0 )
				++j;
			res[i] = min(res[i], N1-(j-k));
		}
	}
}

void prepare_input();
int main() {
	prepare_input();
	
	int ntc; GI(ntc);
	FORE(tc, 1, ntc) {
		solve();
		printf("Case #%d:\n", tc);
		fprintf(stderr, "Case #%d:\n", tc);
		FI printf("%d\n", res[i]);
	}
}


void prepare_input()  {
	bool LOCAL = false;
	char TASK = 'C';

	static char in_file[200], out_file[200];
	if (LOCAL) {
		freopen("input.txt", "rt", stdin);
	} else {

		int ATTEMPT = 0;
		bool LARGE = true;

		if (LARGE) {
			sprintf(in_file, "%c-large.in", TASK);
			sprintf(out_file, "%c-large.out", TASK);
		} else {
			sprintf(in_file, "%c-small-attempt%d.in", TASK,  ATTEMPT);
			sprintf(out_file, "%c-small-attempt%d.out", TASK,  ATTEMPT);
		}

		cerr << in_file <<  endl; freopen(in_file, "rt", stdin);
		cerr << out_file << endl; freopen(out_file, "w", stdout);
	}
}
