#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <queue>
#include <map>
#define FI first
#define SE second
using namespace std;
const double EPS = 1e-8;
const int MAXN = 1005;
const int INF = 1111111111;
int fabs(double x, double y) {
    if (abs(x-y) < EPS) return 0;
    if (x - y > 0) return 1;
    return -1;
}
int main() {
    //freopen("F:\\retired\\gcj2015\\B-large.in","r",stdin);
    freopen("F:\\retired\\gcj2015\\in.txt","r",stdin);
    freopen("F:\\retired\\gcj2015\\out.txt","w",stdout);
    int cas;
    int n;
    double v, x;
    double c1, c2, r1, r2;
    int pan[MAXN];
    cin>>cas;
    for (int ca = 1; ca <= cas; ++ca) {
        cin>>n>>v>>x;
        if (n == 1) {
            cin>>r1>>c1;
            if (fabs(x, c1) == 0) {
                printf("Case #%d: %.10f\n", ca, v / r1);
            } else {
                printf("Case #%d: IMPOSSIBLE\n", ca);
            }
        } else {
            cin>>r1>>c1>>r2>>c2;
            if ((fabs(c1, x) > 0 && fabs(c2, x) > 0) || (fabs(c1, x) < 0 && fabs(c2, x) < 0)) {
                printf("Case #%d: IMPOSSIBLE\n", ca);
            } else if (fabs(c1, x) == 0 && fabs(c2, x) == 0) {
                printf("Case #%d: %.10f\n", ca, v / (r1+ r2));
            } else {
                double a = (x - c2) / (c1 - c2);
                double v1 = v * a, v2 = v * (1 - a);
                printf("Case #%d: %.10f\n", ca, max(v1 / r1, v2 / r2));
            }
        }

    }
    return 0;
}
