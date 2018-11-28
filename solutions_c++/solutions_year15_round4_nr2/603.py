#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define FI first
#define SE second
using namespace std;
typedef long long LL;

inline int sgn(double x) {
    if(x < -eps) return -1;
    return x > eps;
}

int main() {
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int ca = 1; ca <= T; ++ca) {
        int n;
        scanf("%d", &n);
        double X, V;
        scanf("%lf%lf", &V, &X);
        double R[2], C[2];
        for(int i = 0; i < n; ++i) scanf("%lf%lf", R + i, C + i);
        printf("Case #%d: ", ca);
        if(n == 1) {
            if(sgn(X - C[0]) != 0) {
                puts("IMPOSSIBLE");
            }
            else {
                printf("%.10f\n", V / R[0]);
            }
            continue;
        }
        double v1 = max(C[0], C[1]);
        double v2 = min(C[0], C[1]);
        if(sgn(v1 - X) < 0 || sgn(v2 - X) > 0) {
            puts("IMPOSSIBLE");
            continue;
        }
        if(sgn(C[0] - C[1]) == 0) {
            printf("%.10f\n", V / (R[0] + R[1]));
            continue;
        }
        X *= V;
        v1 = (X - V * C[0]) / (C[1] - C[0]);
        v2 = V - v1;
        printf("%.10f\n", max(v1 / R[1], v2 / R[0]));
    }
    return 0;
}
