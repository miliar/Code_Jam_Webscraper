#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

const double EPS = 1e-8;
const double PI = acos(-1.0);

inline double sqr(double x) {
	return x * x;
}

inline bool zero(double x) {
	return x > -EPS && x < EPS;
}

inline bool eq(double x, double y) {
	return x < y + EPS && y < x + EPS;
}

inline int sgn(double x) {
	return x > EPS ? 1 : (x > -EPS ? 0 : -1);
}

struct Point {
	double x, y;
	static Point ZERO;

	Point(double x = 0, double y = 0) : x(x), y(y) {}

	Point operator + (const Point& p) const {
		return Point(x + p.x, y + p.y);
	}

	Point operator - (const Point& p) const {
		return Point(x - p.x, y - p.y);
	}

	Point operator * (double k) const {
		return Point(x * k, y * k);
	}

	Point operator / (double k) const {
		return Point(x / k, y / k);
	}

	double operator * (const Point& p) const {
		return x * p.y - y * p.x;
	}

	double operator ^ (const Point& p) const {
		return x * p.x + y * p.y;
	}

	Point& operator += (const Point& p) {
		x += p.x;
		y += p.y;
		return *this;
	}

	Point& operator -= (const Point& p) {
		x -= p.x;
		y -= p.y;
		return *this;
	}

	Point& operator *= (double k) {
		x *= k;
		y *= k;
		return *this;
	}

	Point& operator /= (double k) {
		x /= k;
		y /= k;
		return *this;
	}

	Point pvec() const {
		return Point(-y, x);
	}

	double len() const {
		return hypot(x, y);
	}

	double sqrlen() const {
		return x * x + y * y;
	}

	Point trunc(double k) const {
		return *this * (k / len());
	}

	// 逆时针旋转a角度
	Point rotate(double a) const {
		Point p(sin(a), cos(a));
		return Point(*this * p, *this ^ p);
	}

	// 旋转至以p向量与x轴重合
	Point rotate(const Point& p) const {
		Point q = Point(-p.y, p.x).trunc(1.0);
		return Point(*this * q, *this ^ q);
	}

	bool operator < (const Point& p) const {
		return x < p.x - EPS || (x < p.x + EPS && y < p.y - EPS);
	}

	bool operator == (const Point& p) const {
		return eq(x, p.x) && eq(y, p.y);
	}

	bool operator != (const Point& p) const {
		return !eq(x, p.x) || !eq(y, p.y);
	}
};

Point Point::ZERO = Point(0.0, 0.0);

inline int decideSide(const Point& p1, const Point& p2, const Point& l1, const Point& l2) {
	return sgn((l2 - l1) * (p1 - l1)) * sgn((l2 - l1) * (p2 - l1));
}

inline int dotsOnline(const Point& p, const Point& l1, const Point& l2) {
	return !zero((l1 - p) * (l2 - p)) ? -1 : (p == l1 || p == l2 ? 0 : (((l2 - p) ^ (l1 - p)) < 0 ? 1 : -1));
}

inline int cross(const Point& u1, const Point& u2, const Point& v1, const Point& v2) {
	return decideSide(u1, u2, v1, v2) < 0 && decideSide(v1, v2, u1, u2) < 0 ? 1 : (dotsOnline(u1, v1, v2) >= 0 || dotsOnline(u2, v1, v2) >= 0 || dotsOnline(v1, u1, u2) >= 0 || dotsOnline(v2, u1, u2) >= 0 ? 0 : -1);
}

inline int convexHall(int n, Point p[], Point q[], bool cl = false) {
	if (n < 3) {
		memcpy(q, p, sizeof(Point) * n);
		return n;
	} else {
		const double eps = cl ? -EPS : EPS;
		int c;
		sort(p, p + n);
		for (int i = c = 0; i < n; q[c++] = p[i++]) {
			for (; c > 1 && (q[c - 1] - q[c - 2]) * (p[i] - q[c - 1]) < eps; --c);
		}
		for (int i = n - 2, j = c; i >= 0; q[c++] = p[i--]) {
			for (; c > j && (q[c - 1] - q[c - 2]) * (p[i] - q[c - 1]) < eps; --c);
		}
		return c - 1;
	}
}

inline double calcArea(int n, Point p[]) {
    double res = 0.0;
    for (int i = 0; i < n; ++i) {
        res += p[i] * p[(i + 1) % n];
    }
    res /= 2;
    return fabs(res);
}

int T, n;
int perm[11];
Point p[11], q[11], ch[11];

int main() {
    scanf("%d", &T);
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%lf%lf", &p[i].x, &p[i].y);
            q[i] = p[i];
        }
        int m = convexHall(n, q, ch);
        double half = calcArea(m, ch) / 2;
        for (int i = 0; i < n; ++i) {
            perm[i] = i;
        }
        do {
            Point ps[11];
            for (int i = 0; i < n; ++i) {
                ps[i] = p[perm[i]];
            }
            ps[n] = ps[0];
            bool ok = true;
            for (int i = 0; i < n && ok; ++i) {
                for (int j = 0; j < n && ok; ++j) {
                    if (i != j && i != (j + 1) % n && j != (i + 1) % n) {
                        int t = cross(ps[i], ps[i + 1], ps[j], ps[j + 1]);
                        if (t != -1) {
                            ok = false;
                        }
                    }
                }
            }
            if (ok && calcArea(n, ps) > half +EPS) {
                break;
            }
        } while (next_permutation(perm, perm + n));
        printf("Case #%d:", caseNum);
        for (int i = 0; i < n; ++i) {
            printf(" %d", perm[i]);
        }
        printf("\n");
    }
    return 0;
}
