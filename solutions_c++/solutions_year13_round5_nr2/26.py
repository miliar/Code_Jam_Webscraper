#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <iostream>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cctype>
#include <sstream>
#include <cassert>
#include <bitset>
#include <memory.h>
#include <complex>
#include <iomanip>

using namespace std;

#pragma comment(linker, "/STACK:200000000")

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define fore(i, a, n) for(int i = (int)(a); i < (int)(n); i++)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) (int(a.size()) - 1)
#define all(a) a.begin(), a.end()

const double EPS = 1E-9;
const int INF = 1000000000;
const int64 INF64 = (int64) 1E18;
const double PI = 3.1415926535897932384626433832795;

char buf[11000000];

const int NMAX = 15;

struct pt {
  double x, y;

  pt() {}
  pt(double x, double y): x(x), y(y) {}

  bool operator< (const pt& p) const {
    return x < p.x - EPS || abs(x - p.x) < EPS && y < p.y - EPS;
  }

  bool operator== (const pt& p) const {
    return abs(x - p.x) < EPS && abs(y - p.y) < EPS;
  }
};

struct line {
	double a, b, c;

	line() {}
	line (pt p, pt q) {
		a = p.y - q.y;
		b = q.x - p.x;
		c = - a * p.x - b * p.y;
		double z = sqrt (a*a + b*b);
		if (abs(z) > EPS)
			a /= z,  b /= z,  c /= z;
	}
	double dist (pt p) {
		return a * p.x + b * p.y + c;
	}
};

double vec (pt a, pt b, pt c) {
	return (b.x - a.x) * (c.y - a.y)
			- (b.y - a.y) * (c.x - a.x);
}

#define det(a,b,c,d)  (a*d-b*c)

bool betw (double l, double r, double x) {
	return min(l,r) <= x + EPS
			&& x <= max(l,r) + EPS;
}

bool intersect (double a, double b,
		double c, double d)
{
	if (a > b)  swap (a, b);
	if (c > d)  swap (c, d);
	return max (a, c) <= min (b, d) + EPS;
}

int intersect (pt a, pt b, pt c, pt d,
		pt & left, pt & right)
{
	if (! intersect (a.x, b.x, c.x, d.x)
				|| ! intersect (a.y, b.y, c.y, d.y))
		return 0;
	line m (a, b);
	line n (c, d);
	double zn = det (m.a, m.b, n.a, n.b);
	if (abs (zn) < EPS) {
		if (abs (m.dist (c)) > EPS
				|| abs (n.dist (a)) > EPS)
			return 0;
		if (b < a)  swap (a, b);
		if (d < c)  swap (c, d);
		left = max (a, c);
		right = min (b, d);
		return (left < right) ? 2 : 1;
	}
	left.x = right.x =
					- det (m.c, m.b, n.c, n.b) / zn;
	left.y = right.y =
					- det (m.a, m.c, n.a, n.c) / zn;
	return betw (a.x, b.x, left.x)
		&& betw (a.y, b.y, left.y)
		&& betw (c.x, d.x, left.x)
		&& betw (c.y, d.y, left.y);
}

pt a[NMAX];
int p[NMAX], n, best[NMAX];
double ans;
bool u[NMAX];

void read() {
  cin >> n;
  forn(i, n)
    cin >> a[i].x >> a[i].y;
}

bool common_endpoint(pt a, pt b, pt c, pt d) {
  return a == c || a == d || b == c || b == d;
}

bool check(pt a, pt b, pt c, pt d) {
  pt p1, p2;
  int cnt = intersect(a, b, c, d, p1, p2);

  if (cnt == 0)
    return true;
  if (cnt == 2)
    return false;

  return common_endpoint(a, b, c, d);
}

double area() {
  double res = 0;
  forn(i, n)
    res += vec(pt(0, 0), a[p[i]], a[p[(i + 1) % n]]);

  return abs(res);
}

void rec(int cur, int pos) {
  if (pos == n) {
    forn(i, n - 1)
      if (!check(a[p[i]], a[p[i + 1]], a[0], a[cur]))
        return;

    double c = area();
    if (ans < c) {
      ans = c;
      memcpy(best, p, sizeof(p));
    }
    return;
  }

  forn(i, n)
    if (!u[i]) {
      bool ok = true;
      forn(j, pos - 1)
        if (!check(a[p[j]], a[p[j + 1]], a[cur], a[i])) {
          ok = false;
          break;
        }

      if (ok) {
        u[i] = true;
        p[pos] = i;
        rec(i, pos + 1);
        u[i] = false;
      }
    }
}

void solve() {
  memset(u, 0, sizeof(u));
  u[0] = true;
  ans = 0;
  rec(0, 1);

  forn(i, n)
    printf(" %d", best[i]);
  puts("");
}

int main() {
#ifdef RADs_project
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
#endif
  
  int tests;
  scanf("%d", &tests);
  gets(buf);

  for (int test = 1; test <= tests; test++) {
    cerr << "Test " << test << " of " << tests << ": " << clock() << endl;

    cout << "Case #" << test << ":";

    read();
    //gen();
    solve();
  }

  cerr << "Total time: " << clock() << endl;
  
  return 0;
}