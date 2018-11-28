#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

// f[i][j][k] denotes 前i行，状态为j，总房间数为k的最小代价

int n;
double V, X;
double r[1000], x[1000];
double v1, v2, t1, t2;
void work()
{
    scanf("%d%lf%lf", &n, &V, &X);
    for (int i = 0; i < n; i++) {
        scanf("%lf%lf", &r[i], &x[i]);
    }
    if (n == 1) {
        if (x[0] != X) {
            puts("IMPOSSIBLE");
            return;
        }
        printf("%.10lf\n", V / r[0]);
    } else {
        if ((x[0] - X) * (x[1] - X) > 0) {
            puts("IMPOSSIBLE");
            return;
        }
        if (X != x[0] && X != x[1]) {
            v2 = V * (1 - X / x[0])/ (1 - x[1]/x[0]);
            v1 = V - v2;
//          printf("%lf\n", (v1 * x[0] + v2 * x[1]) / (v1 + v2));
            t1 = v1 / r[0];
            t2 = v2 / r[1];
            printf("%.10lf\n", max(t1, t2));
        } else if (X == x[0] && X == x[1]) {
            printf("%.10lf\n", V / (r[0] + r[1]));
        } else {
            if (X == x[0]) {
                printf("%.10lf\n", V / (r[0]));
            }
            if (X == x[1]) {
                printf("%.10lf\n", V / (r[1]));                
            }
        }
    }
}
int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
        work();
    }
    return 0;
}