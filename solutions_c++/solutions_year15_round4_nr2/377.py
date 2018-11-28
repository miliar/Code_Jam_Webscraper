#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <set>
using namespace std;

int n;
double V, T;
double r[200];
double t[200];

bool check(double tot) {
    double more = 0;
    double less = 0;
    double totv = 0;
    for (int i = 0; i < n; i++) {
        if (t[i] >= T) {
            more += (t[i] - T) * tot * r[i];
        } else {
            less += (T - t[i]) * tot * r[i];
        }
        totv += tot * r[i];
    }
    for (int i = n - 1; i >= 0; i--) {
        if (t[i] > T && more > less) {
            double c = (t[i] - T) * tot * r[i];
            if (c < more - less) {
                more -= c;
                totv -= tot * r[i];
            } else {
                totv -= (more - less) / (t[i] - T);
                break;
            }
        } else if (t[i] < T && less > more) {
            double c = (T - t[i]) * tot * r[i];
            if (c < less - more) {
                less -= c;
                totv -= tot * r[i];
            } else {
                totv -= (less - more) / (T - t[i]);
                break;
            }
        }
    }
    return totv >= V;
}

struct node {
    double r;
    double t;
};
bool cmp(const node& a, const node& b) {
    return fabs(T - a.t) < fabs(T - b.t);
}
bool cmp2(const node& a, const node& b) {
    return a.t < b.t;
}
node tmp[200];

void solve() {
    scanf("%d%lf%lf", &n, &V, &T);
    for (int i = 0; i < n; i++) {
        scanf("%lf%lf", &tmp[i].r, &tmp[i].t);
    }
    sort(tmp, tmp + n, cmp2);
    if (tmp[0].t > T || tmp[n - 1].t < T) {
        printf("IMPOSSIBLE\n");
        return;
    }
    sort(tmp, tmp + n, cmp);
    for (int i = 0; i < n; i++) {
        r[i] = tmp[i].r;
        t[i] = tmp[i].t;
    }
    double l = 0;
    double r = 1e30;
    for (int k = 0; k < 100000; k++) {
        double mid = (l + r) / 2;
        if (check(mid))
            r = mid;
        else
            l = mid;
    }
    printf("%.9lf\n", l);
}

int main() {
    freopen("E:/1.in", "r", stdin);
    freopen("E:/1.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
