#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

#define MAX 3005

#define mp make_pair
#define fi first
#define se second

typedef pair<int, int> pii;

struct Point {
    long long x, y;
    int id;
    Point() {}
    Point(long long x, long long y, int id = -1) : x(x), y(y), id(id) {}
    Point operator-(const Point &o) const {
        return Point(x - o.x, y - o.y);
    }
    long long operator%(const Point &o) const {
        return x * o.y - o.x * y;
    }
    bool operator<(const Point &o) const {
        return x != o.x ? x < o.x : y < o.y;
    }
};

long long ccw(Point p, Point q, Point r) {
    return (q - p) % (r - p);
}

int n, x[MAX], y[MAX];
int qnt, m;
Point pnts[MAX], hull[MAX];

bool ch(int id) {
    sort(pnts, pnts+qnt);
    m = 0;
    hull[m++] = pnts[0];
    for (int i = 1; i < qnt; i++) {
        if (i != qnt-1 && ccw(pnts[0], pnts[qnt-1], pnts[i]) > 0) continue;
        while (m > 1 && ccw(hull[m-2], hull[m-1], pnts[i]) < 0) m--;
        hull[m++] = pnts[i];
    }
    for (int i = qnt-2; i >= 0; i--) {
        if (i != 0 && ccw(pnts[qnt-1], pnts[0], pnts[i]) > 0) continue;
        while (m > 1 && ccw(hull[m-2], hull[m-1], pnts[i]) < 0) m--;
        hull[m++] = pnts[i];
    }
    for (int i = 0; i < m; i++)
        if (hull[i].id == id)
            return true;
    return false;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%d %d", &x[i], &y[i]);
        printf("Case #%d:\n", t);
        for (int i = 0; i < n; i++) {
            int ans = n-1;
            for (int mask = 0; mask < 1 << n; mask++) {
                if (~mask & 1 << i) continue;
                qnt = 0;
                for (int k = 0; k < n; k++)
                    if (mask & 1 << k)
                        pnts[qnt++] = Point(x[k], y[k], k);
                if (qnt <= 3)
                    ans = min(ans, n - qnt);
                else if (ch(i))
                    ans = min(ans, n - qnt);
            }
            printf("%d\n", ans);
        }
    }
}
