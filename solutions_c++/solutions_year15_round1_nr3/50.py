#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <cassert>
#include <limits>
#include <functional>
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) __typeof(v) r = (v)
#endif
#define each(it,o) for(aut(it, (o).begin()); it != (o).end(); ++ it)
#define all(o) (o).begin(), (o).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
using namespace std;
typedef vector<int> vi; typedef pair<int,int> pii; typedef vector<pair<int,int> > vpii; typedef long long ll;
template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }

struct P {
	typedef int T; typedef ll T2;	//T2��{a*b | a:T, b:T}���܂ރ^�C�v
	T x, y;
	P(T x_, T y_): x(x_), y(y_) {}
	P(): x(0), y(0) {}
};
inline bool operator==(const P& a, const P& b) { return a.x == b.x && a.y == b.y; }
inline bool operator<(const P& a, const P& b) { return a.x < b.x || (a.x == b.x && a.y < b.y); }
inline P operator+(const P& a, const P& b) { return P(a.x+b.x, a.y+b.y); }
inline P operator-(const P& a, const P& b) { return P(a.x-b.x, a.y-b.y); }
inline P operator-=(P& a, const P& b) { a.x -= b.x, a.y -= b.y ; return a; }
inline P::T2 cross(const P& a, const P& b) { return (P::T2)a.x*b.y - (P::T2)a.y*b.x; }
inline P::T2 dot(const P& a, const P& b) { return (P::T2)a.x*b.x + (P::T2)a.y*b.y; }
inline P::T2 norm(const P& a) { return (P::T2)a.x*a.x + (P::T2)a.y*a.y; }
ostream& operator<<(ostream& out, const P& x) { out << "(" << x.x << ", " << x.y << ")"; return out; }


int compareAngle(const P &a, const P &b) {
	int za = a.y > 0 || (a.y == 0 && a.x > 0) ? 0 : 1;
	int zb = b.y > 0 || (b.y == 0 && b.x > 0) ? 0 : 1;
	if(za != zb) return za - zb;
	P::T2 t1 = (P::T2)a.x * b.y;
	P::T2 t2 = (P::T2)a.y * b.x;
	return t1 > t2 ? 1 : t1 < t2 ? -1 : 0;
}

struct Angle {
	P point;
	int infty;
	int eps;
	Angle(): point(), infty(0), eps(0) { }
	Angle(P::T x, P::T y, int eps_ = 0): point(P(x, y)), infty(0), eps(eps_) { }
	Angle(P point_, int eps_ = 0): point(point_), infty(0), eps(eps_) { }
	Angle(P origin, P target, int eps_ = 0): point(target.x - origin.x, target.y - origin.y), infty(0), eps(eps_) { }
	explicit Angle(int infty_): point(), infty(infty_), eps(0) { }
	bool zero() const { return point.x == 0 && point.y == 0; }
	int compare_to(const Angle &that) const {
		if(infty != 0)
			return that.infty == 0 ? infty : (infty > 0) - (that.infty > 0);
		else if(that.infty != 0)
			return -that.infty;
		int t = compareAngle(point, that.point);
		if(t != 0)
			return t;
		return eps == that.eps ? 0 : eps > that.eps ? 1 : -1;
	}
	bool operator==(const Angle &that) const { return compare_to(that) == 0; }
	bool operator!=(const Angle &that) const { return compare_to(that) != 0; }
	bool operator< (const Angle &that) const { return compare_to(that) <  0; }
	bool operator<=(const Angle &that) const { return compare_to(that) <= 0; }
	bool operator> (const Angle &that) const { return compare_to(that) >  0; }
	bool operator>=(const Angle &that) const { return compare_to(that) >= 0; }
	friend ostream &operator<<(ostream &o, const Angle &a) {
		if(a.infty != 0)
			return o << (a.infty > 0 ? "+" : "-") << "oo";
		o << "(" << a.point.x << ", " << a.point.y << ")";
		if(a.eps != 0) o << a.eps;
		return o;
	}
	Angle operator-() const {
		if(infty != 0)
			return Angle(-infty);
		return Angle(-point.x, -point.y, -eps);
	}
};


inline int ccw(const P& a, const P& b, const P& c) {
	int ax = b.x - a.x, ay = b.y - a.y, bx = c.x - a.x, by = c.y - a.y;
	P::T2 t = (P::T2)ax*by - (P::T2)ay*bx;
	if (t > 0) return 1;
	if (t < 0) return -1;
	if((P::T2)ax*bx + (P::T2)ay*by < 0) return +2;
	if((P::T2)ax*ax + (P::T2)ay*ay < (P::T2)bx*bx + (P::T2)by*by) return -2;
	return 0;
}

vector<P> convex_hull(vector<P> ps) {
	int n = ps.size(), k = 0;
	sort(ps.begin(), ps.end());
	vector<P> ch(2*n);
	for (int i = 0; i < n; ch[k++] = ps[i++]) // lower-hull
		while (k >= 2 && ccw(ch[k-2], ch[k-1], ps[i]) <= 0) --k;
	for (int i = n-2, t = k+1; i >= 0; ch[k++] = ps[i--]) // upper-hull
		while (k >= t && ccw(ch[k-2], ch[k-1], ps[i]) <= 0) --k;
	ch.resize(k-1);
	return ch;
}

vector<int> solveSmall(const vector<P> &points) {
	int N = points.size();
	vector<P> v;
	vector<int> ans(N, INF);
	rep(i, 1 << N) if(i != 0) {
		v.clear();
		int p = N;
		rep(j, N) if(i >> j & 1) {
			v.push_back(points[j]);
			-- p;
		}
		vector<P> h = v.size() == 1 ? v : convex_hull(v);
//		cerr << i << ": "; geovis(cerr, h); cerr << endl;
		rep(k, N) if(i >> k & 1) rep(j, h.size()) {
			int c = ccw(h[j], points[k], h[(j+1)%h.size()]);
			if(points[k] == h[j] || c == -2)
				amin(ans[k], p);
		}
	}
	return ans;
}

vector<int> solveLarge(const vector<P> &points) {
	int N = points.size();
	if(N == 1)
		return vector<int>(1, 0);
	vector<Angle> sorted;
	vector<int> ans(N, INF);
	rep(i, N) {
		sorted.clear();
		rep(j, N) if(j != i)
			sorted.push_back(Angle(points[i], points[j]));
		sort(all(sorted));
		sorted.resize((N-1) * 2);
		rep(j, N-1) sorted[N-1+j] = sorted[j];
		if(sorted[0] == sorted[N-2]) {
			ans[i] = 0;
			continue;
		}
		for(int j = 0, k = 0; j < N-1; ++ j) {
			for(; k < N - 1 + j; ++ k) {
				if(sorted[j] < -sorted[j]) {
					if(!(sorted[j] <= sorted[k] && sorted[k] <= -sorted[j]))
						break;
				}else {
					if(!(sorted[j] <= sorted[k] || sorted[k] <= -sorted[j]))
						break;
				}
			}
			amin(ans[i], N - 1 - (k - j));
		}
	}
	return ans;
}

int main() {
	int T;
	scanf("%d", &T);
	rep(ii, T) {
		int N;
		scanf("%d", &N);
		vector<P> points(N);
		rep(i, N) {
			int X, Y;
			scanf("%d%d", &X, &Y);
			points[i] = P(X, Y);
		}
		/*
		rep(i, N) {
			stringstream ss;
			ss << i+1;
			geovis(cerr, points[i], ss.str().c_str());
		}*/
		vector<int> ans = solveLarge(points);
		printf("Case #%d:\n", ii+1);
		rep(i, N) printf("%d\n", ans[i]);
	}
	return 0;
}
