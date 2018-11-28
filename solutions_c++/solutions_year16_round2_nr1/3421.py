// IO
#include <iostream>
#include <fstream>
#include <stdio.h>

#include <vector>
#include <cmath>
#include <algorithm>

#define EPS 0.00000000001
#define PI 3.14159265358979323846
#define PI2 6.283185307179586232

using namespace std;

// coor - geometry coordinate type; calc - geometry calculations type.
typedef long double coor;
typedef long double calc;

struct Vec;
calc cpr(const Vec &v1, const Vec &v2);

template<class Num>
int eq(Num a, Num b)
{
    if (abs(a - b) < EPS) {
        return 1;
    } else {
        return 0;
    }
}

struct Vec {
    coor x, y;

    Vec(): x(0), y(0) {}

    Vec(coor x0, coor y0): x(x0), y(y0) {}

    calc len2() {
        return x * x + y * y;
    }

    calc len() {
        return sqrt(len2());
    }

    Vec operator + (const Vec &v) const {
        return Vec(x + v.x, y + v.y);
    }

    Vec operator - (const Vec &v) const {
        return Vec(x - v.x, y - v.y);
    }

    Vec operator * (calc k) const {
        return Vec(coor(x * k), coor(y * k));
    }

    Vec dir() {
        calc d = 1/len();
        return Vec(coor(x * d), coor(y * d));
    }

    bool operator < (const Vec v) const {
        return y < v.y && eq(x, v.x) && !eq(y, v.y) || x < v.x;
    }

    bool operator > (const Vec v) const {
        return y > v.y && eq(x, v.x) && !eq(y, v.y) || x > v.x;
    }

    bool operator == (const Vec v) const {
        return eq(x, v.x) && eq(y, v.y);
    }

    bool operator >= (const Vec v) const {
        return (*this > v) || (*this == v);
    }

    bool operator <= (const Vec v) const {
        return (*this < v) || (*this == v);
    }

    bool operator != (const Vec v) const {
        return !(*this == v);
    }

    // Parallel vectors
    bool operator || (const Vec &v) const {
        return cpr(*this, v) == 0;
    }
};


ostream &operator << (ostream &out, const Vec &a) {
    out << a.x << " " << a.y << " ";
    return out;
}


istream &operator >> (istream &in, Vec &a) {
    in >> a.x >> a.y;
    return in;
}


struct Line {
    Vec A, B;

    calc k[3];

    Line() {
        k[0] = 0;
        k[1] = 0;
        k[2] = 0;
    }

    Line(calc a, calc b, calc c) {
        // Universal form
        if (c != 0) {
            k[0] = a / c;
            k[1] = b / c;
            k[2] = 1;
        } else if (b != 0) {
            k[0] = a / b;
            k[1] = 1;
            k[2] = 0;
        } else if (a != 0) {
            k[0] = 1;
            k[1] = 0;
            k[2] = 0;
        } else {
            k[0] = 0;
            k[1] = 0;
            k[2] = 0;
        }
        // Two points on the line
        if (a != 0) {
            A = Vec(-c / a, 0);
        }
        if (b != 0) {
            A = Vec(0, -c / b);
        }
        B = A + dir();
    }

    Vec norm() const {
        return Vec(coor(k[0]), coor(k[1]));
    }

    Vec dir() const {
        return Vec(-coor(k[1]), coor(k[0]));
    }

    bool contains(const Vec &v) const {
        return eq(v.x * k[0] + v.y * k[1], -k[2]);
    }

    bool operator == (const Line l) const {
        return eq(k[0], l.k[0]) && eq(k[1], l.k[1]) && eq(k[2], l.k[2]);
    }
};

ostream &operator << (ostream &out, const Line &l) {
    out << l.k[0] << " " << l.k[1] << " " << l.k[2] << " ";
    return out;
}

istream &operator >> (istream &in, Line &l) {
    in >> l.k[0] >> l.k[1] >> l.k[2];
    l = Line(l.k[0], l.k[1], l.k[2]);
    return in;
}


// Point and direction
Line line_pd(const Vec &p, const Vec &d)
{
    Line res;
    if (d != Vec(0, 0)) {
        res = Line(d.y, -d.x, d.x * p.y - d.y * p.x);
        res.A = p;
        res.B = p + d;
    }
    return res;
}


// Two points
Line line_2p(const Vec &v1, const Vec &v2)
{
    Line res;
    if (v1 != v2) {
        res = Line(v2.y - v1.y, v1.x - v2.x, v1.y * (v2.x - v1.x) - v1.x * (v2.y - v1.y));
        res.A = v1;
        res.B = v2;
    }
    return res;
}


// Line intersection: returns <1, Vec> if there's 1 point; <0, (0, 0)> if none; <2, (0, 0)> if infinity.
pair<int, Vec> line_intersect(const Line &l1, const Line &l2)
{
    if (l1 == l2) {
        return make_pair(2, Vec(0, 0));
    } else if (eq(l1.k[0] * l2.k[1], l1.k[1] * l2.k[0])) {
        return make_pair(0, Vec(0, 0));
    } else {
        coor x = coor((-l2.k[1] * l1.k[2] + l1.k[1] * l2.k[2]) / (l1.k[0] * l2.k[1] - l2.k[0] * l1.k[1]));
        coor y = coor((-l1.k[0] * l2.k[2] + l2.k[0] * l1.k[2]) / (l1.k[0] * l2.k[1] - l2.k[0] * l1.k[1]));
        return make_pair(1, Vec(x, y));
    }
}


// Intersects the line and its normal containing point v
Vec v_normal(const Vec &v, const Line &l)
{
    return line_intersect(l, line_pd(v, l.norm())).second;
}


// Segment
struct Seg {
    Line l;

    Vec p1, p2;

    Seg(const Vec &v1, const Vec &v2) {
        l = line_2p(v1, v2);
        if (v1 <= v2) {
            p1 = Vec(v1.x, v1.y);
            p2 = Vec(v2.x, v2.y);
        } else {
            p2 = Vec(v1.x, v1.y);
            p1 = Vec(v2.x, v2.y);
        }
    }

    // Envelopes
    bool env(const Vec &v) const {
        return p1 <= v && v <= p2;
    }

    // Returns the point that divides the given segment
    Vec divide(calc a, calc b) {
        return p1 + ((p2 - p1) * (a / (a + b)));
    }
};


// Segment intersection
void seg_intersect(Seg a, Seg b)
{
    if (a.p1 == a.p2 && b.p1 == b.p2) {
        if (a.p1 == b.p1) {
            cout << b.p1;
        } else {
            cout << "Empty";
        }
    } else if (a.p1 != a.p2 && b.p1 == b.p2) {
        if (a.l.contains(b.p1) && a.env(b.p1)) {
            cout << b.p1;
        } else {
            cout << "Empty";
        }
    } else if (b.p1 != b.p2 && a.p1 == a.p2) {
        if (b.l.contains(a.p1) && b.env(a.p1)) {
            cout << a.p1;
        } else {
            cout << "Empty";
        }
    } else {
        pair<int, Vec> cross = line_intersect(a.l, b.l);
        if (cross.first) {
            if (a.env(cross.second) && b.env(cross.second)) {
                cout << cross.second;
            } else {
                cout << "Empty";
            }
        } else if (cross.second == Vec(1, 1)) {
            if (b.p1 < a.p1) {
                swap(a, b);
            }
            if (a.p2 < b.p1) {
                cout << "Empty";
            } else if (a.p2 == b.p1) {
                cout << a.p2;
            } else if (b.p1 < a.p2) {
                cout << b.p1;
                if (b.p2 > a.p2) {
                    cout << a.p2;
                } else {
                    cout << b.p2;
                }
            } else {
                cout << "Empty";
            }
        } else {
            cout << "Empty";
        }
    }
}


// Dot and cross product
calc dpr(const Vec &v1, const Vec &v2)
{
    return v1.x * v2.x + v1.y * v2.y;
}


calc cpr(const Vec &v1, const Vec &v2)
{
    return v1.x * v2.y - v1.y * v2.x;
}


// Making angles universal - from 0 to 2pi
calc uni(calc angle)
{
    while (angle < 0) {
        angle += PI2;
    }
    while (angle >= PI2) {
        angle -= PI2;
    }
    return angle;
}


// Calculate the angle between vectors
calc at2(Vec a, Vec b)
{
    calc res = atan2l(cpr(a, b), dpr(a, b));
    res = -res;
    return uni(res);
}


calc OrientArea(Vec pol[], int n) {
    calc res = 0;
    for (int i = 1; i < n; i++) {
        res += cpr(pol[i - 1], pol[i]) / 2;
    }
    res += cpr(pol[n - 1], pol[0]) / 2;
    return res;
}


bool cmp (Vec a, Vec b) {
	return a.x < b.x || a.x == b.x && a.y < b.y;
}

bool cw (Vec a, Vec b, Vec c) {
	return a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y) < 0;
}

bool ccw (Vec a, Vec b, Vec c) {
	return a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y) > 0;
}

void convex_hull (vector<Vec> & a) {
	if (a.size() == 1)  return;
	sort (a.begin(), a.end(), &cmp);
	Vec p1 = a[0],  p2 = a.back();
	vector<Vec> up, down;
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


int main()
{

    cout.precision(10);
    cout << fixed;

    int n;
    cin >> n;
    vector<Vec> pts(n);
    for (int i = 0; i < n; i++) {
		cin >> pts[i];
	}
	convex_hull(pts);
	for (int i = 0; i < pts.size(); i++) {
		cout << pts[i] << "\n";
	}

    return 0;
}
