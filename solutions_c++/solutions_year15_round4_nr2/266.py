#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long double ld;
const int kMaxN = 100;

int n;
ld V, X;

struct Point {
    ld x, y;
    Point() {}
    Point(ld _x, ld _y) : x(_x), y(_y) {}
    bool operator<(const Point &t) const {
        return y / x < t.y / t.x;
    }
} p[kMaxN];

const ld kEps = 1e-14;
inline int sgn(ld x) {
    if (fabsl(x) < kEps) return 0;
    if (x > 0) return 1;
    return -1;
}
/*
bool in(const Point &p) {
    if (m == 1) return sgn(p.x - q[0].x) == 0 && sgn(p.y - q[0].y) == 0;
    bool chk = true;
    for (int i = 0; i < m; ++ i) {
        int j = (i + 1) % m;
        Vector v1 = q[j] - q[i];
        Vector v2 = p - q[i];
        if (sgn(det(v1, v2)) >= 0) chk = false;
    }
    if (chk) return true;
    for (int i = 0; i < m; ++ i) {
        int j = (i + 1) % m;
        Vector v1 = q[j] - q[i];
        Vector v2 = p - q[i];
        if (sgn(det(v1, v2)) > 0) return false;
        if (sgn(det(v1, v2)) == 0) {
            if (sgn(dot(q[j] - p, q[i] - p)) > 0) return false;
        }
    }
    return true;
}

void getHull() {
    sort(p, p + n);
    m = 0;
    stop = 0;
    for (int i = 0, j = 0; i < n; i = j) {
        while (j < n && p[j].x == p[i].x) ++ j;
        while (stop >= 2) {
            Vector v2 = p[j - 1] - p[stack[stop - 1]];
            Vector v1 = p[stack[stop - 1]] - p[stack[stop - 2]];
            if (det(v1, v2) < 0) break;
            -- stop;
        }
        stack[stop ++] = j - 1;
    }
    for (int i = 0; i < stop; ++ i) hull[m ++] = stack[i];
    stop = 0;
    for (int i = n - 1, j = n - 1; i >= 0; i = j) {
        while (j >= 0 && p[j].x == p[i].x) -- j;
        while (stop >= 2) {
            Vector v2 = p[j + 1] - p[stack[stop - 1]];
            Vector v1 = p[stack[stop - 1]] - p[stack[stop - 2]];
            if (det(v1, v2) < 0) break;
            -- stop;
        }
        stack[stop ++] = j + 1;
    }
    for (int st = hull[0], ed = hull[m - 1], i = 0; i < stop; ++ i)
        if (stack[i] != st && stack[i] != ed) hull[m ++] = stack[i];
    for (int i = 0; i < m; ++ i) q[i] = p[hull[i]];
}

double aa[kMaxN], bb[kMaxN];
bool check(double T) {
    double A = V / T, B = V * X / T;
    for (int i = 0; i < n; ++ i) {
        if (aa[i] >= A) {
            p[i] = Point(1, A * bb[i] / aa[i]);
        } else {
            p[i] = Point(aa[i] / A, bb[i]);
        }
    }
    getHull();
    return in(Point(1, B));
}*/

bool check(ld T) {
    ld sx = 0.0, sy = 0.0;
    ld A = V, B = V * X;
    for (int i = 0; i < n; ++ i) {
        if (sx + p[i].x * T <= V) {
            sx += p[i].x * T;
            sy += p[i].y * T;
        } else {
            ld t = (V - sx) / p[i].x;
            sx += p[i].x * t;
            sy += p[i].y * t;
            break;
        }
    }
    if (sgn(sx - V) < 0) return false;
    ld lb = sy;
    sx = 0, sy = 0;
    for (int i = n - 1; i >= 0; -- i) {
        if (sx + p[i].x * T <= V) {
            sx += p[i].x * T;
            sy += p[i].y * T;
        } else {
            ld t = (V - sx) / p[i].x;
            sx += p[i].x * t;
            sy += p[i].y * t;
            break;
        }
    }
    if (sgn(sx - V) < 0) return false;
    ld rb = sy;
    return sgn(lb - B) <= 0 && sgn(B - rb) <= 0;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; ++ kase) {
        double a, b;
        scanf("%d%lf%lf", &n, &a, &b);
        V = a, X = b;
        for (int i = 0; i < n; ++ i) {
            scanf("%lf%lf", &a, &b);
            p[i].x = a, p[i].y = b;
            p[i].y *= p[i].x;
        }
        sort(p, p + n);
        printf("Case #%d: ", kase);
        ld lb = 0, rb = 1e9;
        for (int t = 0; t < 2000; ++ t) {
            ld mid = (lb + rb) * 0.5;
            if (check(mid)) {
                rb = mid;
            } else {
                lb = mid;
            }
        }
        if (check(rb)) printf("%.10f\n", (double)rb);
        else puts("IMPOSSIBLE");
    }
    return 0;
}
