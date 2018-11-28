#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;
#define pii pair<int, int>
#define pdd pair<double, double>
#define mp make_pair
#define x first
#define y second
#define L(s) ((int)(s).size())
#define pb push_back
#define VI vector<int>
#define ll long long
#define all(s) (s).begin(), (s).end()
int n, t;
pii a[11];
VI p;

bool cmp (pii a, pii b) {
	return a.x < b.x || a.x == b.x && a.y < b.y;
}

bool cw (pii a, pii b, pii c) {
	return a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y) < 0;
}

bool ccw (pii a, pii b, pii c) {
	return a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y) > 0;
}

void convex_hull (vector<pii> & a) {
	if (a.size() == 1)  return;
	sort (a.begin(), a.end(), &cmp);
	pii p1 = a[0],  p2 = a.back();
	vector<pii> up, down;
	up.push_back (p1);
	down.push_back (p1);
	for (size_t i=1; i<a.size(); ++i) {
		if (i==a.size()-1 || cw (p1, a[i], p2)) {
			while (up.size()>=2 && !cw (up[up.size()-2], up[up.size()-1], a[i]))
				up.pop_back();
			up.push_back (a[i]);
		}
		if (i==a.size()-1 || ccw (p1, a[i], p2)) {
			while (down.size()>=2 && !ccw (down[down.size()-2], down[down.size()-1], a[i]))
				down.pop_back();
			down.push_back (a[i]);
		}
	}
	a.clear();
	for (size_t i=0; i<up.size(); ++i)
		a.push_back (up[i]);
	for (size_t i=down.size()-2; i>0; --i)
		a.push_back (down[i]);
}

double getS(vector<pii> &a) {
	double ans = 0;
	for(int i = 0; i < L(a); ++i) {
		int j = (i + 1) % L(a);
		ans += a[i].x * a[j].y - a[j].x * a[i].y;
	}
	return abs(ans) / 2.;
}

const double EPS = 1E-9;
 
struct pt {
	double x, y;
	pt(double _x, double _y):x(_x),y(_y){}
 
	bool operator< (const pt & p) const {
		return x < p.x-EPS || abs(x-p.x) < EPS && y < p.y - EPS;
	}
};
 
struct line {
	double a, b, c;
 
	line() {}
	line (pt p, pt q) {
		a = p.y - q.y;
		b = q.x - p.x;
		c = - a * p.x - b * p.y;
		norm();
	}
 
	void norm() {
		double z = sqrt (a*a + b*b);
		if (abs(z) > EPS)
			a /= z,  b /= z,  c /= z;
	}
 
	double dist (pt p) const {
		return a * p.x + b * p.y + c;
	}
};
 
#define det(a,b,c,d)  (a*d-b*c)
 
inline bool betw (double l, double r, double x) {
	return min(l,r) <= x + EPS && x <= max(l,r) + EPS;
}
 
inline bool intersect_1d (double a, double b, double c, double d) {
	if (a > b)  swap (a, b);
	if (c > d)  swap (c, d);
	return max (a, c) <= min (b, d) + EPS;
}
 
bool intersect (pt a, pt b, pt c, pt d, pt & left, pt & right) {
	if (! intersect_1d (a.x, b.x, c.x, d.x) || ! intersect_1d (a.y, b.y, c.y, d.y))
		return false;
	line m (a, b);
	line n (c, d);
	double zn = det (m.a, m.b, n.a, n.b);
	if (abs (zn) < EPS) {
		if (abs (m.dist (c)) > EPS || abs (n.dist (a)) > EPS)
			return false;
		if (b < a)  swap (a, b);
		if (d < c)  swap (c, d);
		left = max (a, c);
		right = min (b, d);
		return true;
	}
	else {
		left.x = right.x = - det (m.c, m.b, n.c, n.b) / zn;
		left.y = right.y = - det (m.a, m.c, n.a, n.c) / zn;
		return betw (a.x, b.x, left.x)
			&& betw (a.y, b.y, left.y)
			&& betw (c.x, d.x, left.x)
			&& betw (c.y, d.y, left.y);
	}
}

int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int tc = 1; tc <= t; ++tc) {
		cerr << tc << endl;
		cin >> n;
		p.clear();
		vector<pii> v;
		v.clear();
		for(int i = 0; i < n; ++i) {
			cin >> a[i].x >> a[i].y;
			p.pb(i);
			v.pb(a[i]);
		}
		convex_hull(v);
		double S = getS(v);

		do {
			bool ok = 1;
			vector<pii> ord(0);
			for(int i = 0; i < n; ++i) ord.pb(a[p[i]]);
			for(int i = 0; i < n; ++i) {
				for(int j = 0; j < n; ++j) {
					pt p1(ord[i].x, ord[i].y);
					pt p2(ord[(i + 1) % n].x, ord[(i + 1) % n].y);
					pt q1(ord[j].x, ord[j].y);
					pt q2(ord[(j + 1) % n].x, ord[(j + 1) % n].y);
					pt lf(0,0), rt(0,0);
					if (i == j || (i + 1) % n == j || (j + 1) % n == i || (i + 1) % n == (j + 1) % n) {
						if (i == j) continue;
						if (intersect(p1, p2, q1, q2, lf, rt)) {
							if (abs(lf.x - rt.x) > EPS || abs(lf.y - rt.y) > EPS) ok = 0;
						}
					} else {
						if (intersect(p1, p2, q1, q2, lf, rt)) ok = 0;

					}
				}
			}
			if (ok) {
				double curS = getS(ord);
				if (curS * 2 > S + EPS) {
					printf("Case #%d:", tc);
					for(int i = 0; i < n; ++i) printf(" %d", p[i]);
					printf("\n");
					break;
				}
			}
		} while(next_permutation(all(p)));
		
	}
} 