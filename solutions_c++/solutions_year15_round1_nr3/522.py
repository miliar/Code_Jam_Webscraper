#include <algorithm>
#include <bitset>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

#define repi(i, a, b) for(int i = (a); i < (int)(b); i++)
#define rep(i, a) repi(i, 0, a)
#define repd(i, a, b) for(int i = (a); i >= (int)(b); i--)
#define repit(i, v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define reprit(i, v) for(__typeof((v).rbegin()) i = (v).rbegin(); i != (v).rend(); i++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define uniq(v) (v).erase(unique(all(v)), (v).end())
#define pb push_back
#define mp make_pair

using namespace std;
typedef long long ll;

// constants and eps-considered operators

const double eps = 1e-10; // choose carefully!
const double pi = acos(-1.0);
inline bool lt(double a, double b) { return a < b - eps; }
inline bool gt(double a, double b) { return lt(b, a); }
inline bool le(double a, double b) { return !lt(b, a); }
inline bool ge(double a, double b) { return !lt(a, b); }
inline bool ne(double a, double b) { return lt(a, b) or lt(b, a); }
inline bool eq(double a, double b) { return !ne(a, b); }

// points and lines

typedef complex<double> point;
inline double inner(point a, point b) { return real(conj(a) * b); }
inline double cross(point a, point b) { return imag(conj(a) * b); }
struct line {
  point a, b;
  line(point a, point b) : a(a), b(b) {}
};

/*
 *  Here is what ccw(a, b, c) returns:
 *
 *          1
 *  ------------------
 *    2 |a  0  b| -2
 *  ------------------
 *         -1
 *
 *  Note: we can implement intersectPS(p, s) as !ccw(s.a, s.b, p).
 */
int ccw(point a, point b, point c) {
  b -= a, c -= a;
  if (cross(b, c) > +eps)   return +1;
  if (cross(b, c) < -eps)   return -1;
  if (inner(b, c) < -eps)   return -2; // c -- a -- b
  if (lt(norm(b), norm(c))) return +2; // a -- b -- c
  return 0;
}
bool intersectLS(const line& l, const line& s) {
  return ccw(l.a, l.b, s.a) * ccw(l.a, l.b, s.b) <= 0;
}
bool intersectSS(const line& s, const line& t) {
  return intersectLS(s, t) and intersectLS(t, s);
}
bool intersectLL(const line& l, const line& m) {
  return ne(cross(l.b - l.a, m.b - m.a), 0.0)  // not parallel
    or eq(cross(l.b - l.a, m.a - l.a), 0.0); // overlap
}
point crosspointLL(const line& l, const line& m) {
  double p = cross(l.b - l.a, m.b - m.a);
  double q = cross(l.b - l.a, m.a - l.a);
  if (eq(p, 0.0) and eq(q, 0.0)) return m.a; // overlap
  return m.a - q / p * (m.b - m.a);
}
point proj(const line& l, point p) {
  double t = inner(l.b - l.a, p - l.a) / norm(l.b - l.a);
  return l.a + t * (l.b - l.a);
}
point reflection(const line& l, point p) { return 2.0 * proj(l, p) - p; }

// distances (for shortest path)

double distanceLP(const line& l, point p) { return abs(proj(l, p) - p); }
double distanceLL(const line& l, const line& m) {
  return intersectLL(l, m) ? 0.0 : distanceLP(l, m.a);
}
double distanceLS(const line& l, const line& s) {
  return intersectLS(l, s) ? 0.0 : min(distanceLP(l, s.a), distanceLP(l, s.b));
}
double distancePS(point p, const line& s) {
  point h = proj(s, p);
  return ccw(s.a, s.b, h) ? min(abs(s.a - p), abs(s.b - p)) : abs(h - p);
}
double distanceSS(const line& s, const line& t) {
  if (intersectSS(s, t)) return 0.0;
  return min(min(distancePS(s.a, t), distancePS(s.b, t)),
	     min(distancePS(t.a, s), distancePS(t.b, s)));
}

// circles

struct circle {
  point o; double r;
  circle(point o, double r) : o(o), r(r) {}
};

bool intersectCL(const circle& c, const line& l) {
  return le(norm(proj(l, c.o) - c.o), c.r * c.r);
}
int intersectCS(const circle& c, const line& s) {
  if (not intersectCL(c, s)) return 0;
  double a = abs(s.a - c.o);
  double b = abs(s.b - c.o);
  if (lt(a, c.r) and lt(b, c.r)) return 0;
  if (lt(a, c.r) or lt(b, c.r)) return 1;
  return ccw(s.a, s.b, proj(s, c.o)) ? 0 : 2;
}
bool intersectCC(const circle& c, const circle& d) {
  double dist = abs(d.o - c.o);
  return le(abs(c.r - d.r), dist) and le(dist, c.r + d.r);
}
line crosspointCL(const circle& c, const line& l) {
  point h = proj(l, c.o);
  double a = sqrt(c.r * c.r - norm(h - c.o));
  point d = a * (l.b - l.a) / abs(l.b - l.a);
  return line(h - d, h + d);
}
line crosspointCC(const circle& c, const circle& d) {
  double dist = abs(d.o - c.o), th = arg(d.o - c.o);
  double ph = acos((c.r * c.r + dist * dist - d.r * d.r) / (2.0 * c.r * dist));
  return line(c.o + polar(c.r, th - ph), c.o + polar(c.r, th + ph));
}

line tangent(const circle& c, double th) {
  point h = c.o + polar(c.r, th);
  point d = polar(c.r, th) * point(0, 1);
  return line(h - d, h + d);
}
vector<line> common_tangents(const circle& c, const circle& d) {
  vector<line> ret;
  double dist = abs(d.o - c.o), th = arg(d.o - c.o);
  if (abs(c.r - d.r) < dist) { // outer
    double ph = acos((c.r - d.r) / dist);
    ret.pb(tangent(c, th - ph));
    ret.pb(tangent(c, th + ph));
  }
  if (abs(c.r + d.r) < dist) { // inner
    double ph = acos((c.r + d.r) / dist);
    ret.pb(tangent(c, th - ph));
    ret.pb(tangent(c, th + ph));
  }
  return ret;
}
pair<circle, circle> tangent_circles(const line& l, const line& m, double r) {
  double th = arg(m.b - m.a) - arg(l.b - l.a);
  double ph = (arg(m.b - m.a) + arg(l.b - l.a)) / 2.0;
  point p = crosspointLL(l, m);
  point d = polar(r / sin(th / 2.0), ph);
  return mp(circle(p - d, r), circle(p + d, r));
}
line bisector(point a, point b);
circle circum_circle(point a, point b, point c) {
  point o = crosspointLL(bisector(a, b), bisector(a, c));
  return circle(o, abs(a - o));
}

// polygons

typedef vector<point> polygon;

double area(const polygon& g) {
  double ret = 0.0;
  int j = g.size() - 1;
  rep(i, g.size()) {
    ret += cross(g[j], g[i]), j = i;
  }
  return ret / 2.0;
}
point centroid(const polygon& g) {
  if (g.size() == 1) return g[0];
  if (g.size() == 2) return (g[0] + g[1]) / 2.0;
  point ret = 0.0;
  int j = g.size() - 1;
  rep(i, g.size()) {
    ret += cross(g[j], g[i]) * (g[j] + g[i]), j = i;
  }
  return ret / area(g) / 6.0;
}
line bisector(point a, point b) {
  point m = (a + b) / 2.0;
  return line(m, m + (b - a) * point(0, 1));
}
polygon convex_cut(const polygon& g, const line& l) {
  polygon ret;
  int j = g.size() - 1;
  rep(i, g.size()) {
    if (ccw(l.a, l.b, g[j]) != -1) ret.pb(g[j]);
    if (intersectLS(l, line(g[j], g[i]))) ret.pb(crosspointLL(l, line(g[j], g[i])));
    j = i;
  }
  return ret;
}
polygon voronoi_cell(polygon g, const vector<point>& v, int k) {
  rep(i, v.size()) if (i != k) {
    g = convex_cut(g, bisector(v[i], v[k]));
  }
  return g;
}

namespace std {
  bool operator <(const point& a, const point& b) {
    return ne(real(a), real(b)) ? lt(real(a), real(b)) : lt(imag(a), imag(b));
  }
}

polygon convex_hull(vector<point> v) {
  const int n = v.size();
  sort(all(v));
  polygon ret(2 * n);
  int k = 0;
  for (int i = 0; i < n; ret[k++] = v[i++]) {
    while (k >= 2 and ccw(ret[k - 2], ret[k - 1], v[i]) <= 0) --k;
  }
  for (int i = n - 2, t = k + 1; i >= 0; ret[k++] = v[i--]) {
    while (k >= t and ccw(ret[k - 2], ret[k - 1], v[i]) <= 0) --k;
  }
  ret.resize(k - 1);
  return ret;
}

void solve() {
  int n;
  cin >> n;
  polygon g(n);
  rep(i, n) {
    double x, y;
    cin >> x >> y;
    g[i] = point(x, y);
  }
  cout << endl;

  ll ans = 0;
  rep(k, n) {
    int ans = n-1;
    rep(S, 1<<n) {
      if(((S>>k)&1) == 0) continue;
      bool ok = false;
      polygon ng;      
      rep(i, n) if((S>>i)&1) ng.pb(g[i]);
      polygon ch = convex_hull(ng);

      rep(i, ch.size()) if(abs(ch[i] - g[k]) < eps) {
	ok = true;
	break;
      }
      
      if(ok) {
	int val = __builtin_popcount(S);
	ans = min(ans, n-val);
      }
      
    }
    cout << ans << endl;
  }
  
}

int main() {
  int T;
  cin >> T;
  rep(t, T) {
    cout << "Case #" << t+1 << ":";
    solve();    
  }
  
  return 0;
}
