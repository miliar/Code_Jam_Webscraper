#include <cstdio>
#include <iostream>     // std::cout
#include <limits>       // std::numeric_limits
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;

const double EPS = 1e-8;

double r[3], c[3];

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        double V;
        double C;
        int n;
        cin >> n >> V >> C;

        for (int i = 0; i < n; i++) {
            cin >> r[i] >> c[i];
        }

        if (n == 1) {
            if (fabs(c[0] - C) < EPS) {printf("Case #%d: ", cas); cout <<fixed<<setprecision(10)  << V / r[0] << endl;}
            else printf("Case #%d: IMPOSSIBLE\n", cas);
        } else {
            if (C < min(c[0], c[1]) - EPS || C > max(c[0], c[1]) + EPS) {
                printf("Case #%d: IMPOSSIBLE\n", cas);
                continue;
            }
            if (fabs(c[0] - c[1]) < EPS) {
                printf("Case #%d: ", cas); cout << fixed<<setprecision(10) << V / (r[0] + r[1])<< endl;
                continue;
            }
            int u = 0, v = 1;
            if (c[0] > c[1]) swap(u, v);
            double x = C - c[u];
            double y = c[v] - C;
            printf("Case #%d: ", cas); cout << fixed<<setprecision(10) << max(( double)V *y /( x + y) / r[u],
                                                (double)V * x / (x + y) / r[v]) << endl;



        }
    }
    return 0;
}
