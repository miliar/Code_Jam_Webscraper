#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

struct node { double a, b; };
const double eps = 1e-12;
const int maxn = 1000 + 10;
node d[maxn];
double A, B;
int n;

bool cmp(const node &a, const node &b) {
    return a.b < b.b;
}

int dcmp(double x) {
    return x < -eps ? -1 : x > eps;
}

bool can(double x) {
    double l, r;
    long double rest = A, fenzi = 0, fenmu = 0;
    for (int i = 1; i <= n; ++i) {
        long double use = min((long double)x, rest / d[i].a); rest -= use * d[i].a;
        fenmu += d[i].a * use;
        fenzi += d[i].a * d[i].b * use;
        if (dcmp(rest) == 0) break;
    }
    if (dcmp(rest) != 0) return false;
    l = fenzi / fenmu;
    fenzi = fenmu = 0; rest = A;
    for (int i = n; i; --i) {
        long double use = min((long double)x, rest / d[i].a); rest -= use * d[i].a;
        fenmu += d[i].a * use;
        fenzi += d[i].a * d[i].b * use;
        if (dcmp(rest) == 0) break;
    }
    r = fenzi / fenmu;
    return dcmp(l - B) <= 0 && dcmp(B - r) <= 0;
}

double getans() {
    if (n == 1) {
        double x1 = A / d[1].a;
        double x2 = A * B / d[1].a / d[1].b;
        if (fabs(x1 - x2) < eps) return x1;
        else return -1;
    } else {
        if (!(dcmp(d[1].b - B) <= 0 && dcmp(B - d[n].b) <=0)) return -1;
        long double l = 0, r = 1e10;
        while (l + 1e-11 < r) {
            long double mid = (l + r) * 0.5;
            if (can(mid)) r = mid;
            else l = mid;
        }
        return (l + r) * 0.5;
    }
}

int main() {
    int tt, cas = 0;
    cin >> tt;
    while (tt--) {
        scanf("%d%lf%lf", &n, &A, &B);
        for (int i = 1; i <= n; ++i)
            scanf("%lf%lf", &d[i].a, &d[i].b);
        sort(d + 1, d + 1 + n, cmp);
        printf("Case #%d: ", ++cas);
        double ans = getans();
        if (ans < 0) printf("IMPOSSIBLE\n");
        else printf("%.9lf\n", ans);
    }
}

