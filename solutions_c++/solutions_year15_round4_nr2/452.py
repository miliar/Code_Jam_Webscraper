#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int n;
pair<double, double> source[105];
const double esp = 1e-10;
double V, X;

int check(long double x) {
    static long double v1[105], v2[105];
    long double sum = 0;
    for (int i = 1; i <= n; ++i) {
        v1[i] = (long double)source[i].second * x;
        v2[i] = v1[i];
        sum += v1[i];
    }
    if (sum < V) return 0;
    long double p0 = 0, p1 = 0, q0 = sum - V, q1 = sum - V;
    for (int i = 1; i <= n; ++i) {
        long double tmp = min(v1[i], q0);
        v1[i] -= tmp;
        q0 -= tmp;
        p0 += v1[i] * source[i].first;
    }
    for (int i = n; i >= 1; --i) {
        long double tmp = min(v2[i], q1);
        v2[i] -= tmp;
        q1 -= tmp;
        p1 += v2[i] * source[i].first;
    }
    long double p = X * V;
    if (p1 < p && p0 > p) return 1;
    return 0;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%lf%lf", &n, &V, &X);
        for (int i = 1; i <= n; ++i) {
            scanf("%lf%lf", &source[i].second, &source[i].first);
        }
        sort(source + 1, source + 1 + n);
        static int ca = 0;
        printf("Case #%d: ", ++ca);
        if (source[1].first > X + esp ||
            source[n].first < X - esp) {
            puts("IMPOSSIBLE");
            continue;
        }
        if (fabs(source[1].first - X) < esp ||
            fabs(source[n].first - X) < esp) {
            double ans = 0;
            for (int i = 1; i <= n; ++i)
                if (fabs(source[i].first - X) < esp) {
                     ans += source[i].second;
                }
            ans = V / ans;
            printf("%.10f\n", ans);
            continue;
        }
        long double head = 0, tail = 1e9;
        for (int i = 1; i <= 300; ++i) {
            long double mid = (head + tail) / 2;
            if (check(mid)) tail = mid;
            else head = mid;
        }
        if (head > 1e8 + 1e7) puts("IMPOSSIBLE");
        else printf("%.10f\n", (double)head);
        /*if (n == 2) {
            double V1 = (X * V - source[2].first * V) / (source[1].first - source[2].first);
            double V2 = V - V1;
            double ans = max(V1 / source[1].second, V2 / source[2].second);
            printf("%.10f\n", ans);
            if (ca == 85) {
                printf("%d %.10lf %.10lf\n", n, V, X);
                for (int i = 1; i <= n; ++i)
                    printf("%.10f %.10f\n", source[i].second, source[i].first);
            }
        }
        cout << "----" << endl;
        check(head);*/
    }
    return 0;
}
