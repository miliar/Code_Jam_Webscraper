#include <bits/stdc++.h>
using namespace std;

double dis[1010], g[1010][1010];
int use[1010];
double x[1010], y[1010], z[1010], vx[1010], vy[1010], vz[1010];

double f(int i, int j) {
    double sum = (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]) + (z[i] - z[j]) * (z[i] - z[j]);
    return sqrt(sum);
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n, s;
        scanf("%d%d", &n, &s);
        for (int i = 0; i < n; i++) {
            scanf("%lf%lf%lf%lf%lf%lf", &x[i], &y[i], &z[i], &vx[i], &vy[i], &vz[i]);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                g[i][j] = f(i, j);
            }
        }
        memset(use, 0, sizeof(use));
        for (int i = 0; i < n; i++) {
            dis[i] = 1e50;
        }
        dis[0] = 0.0;
        for (int i = 0; i < n; i++) {
            int id = -1;
            for (int j = 0; j < n; j++) {
                if (use[j]) {
                    continue;
                }
                if (id == -1 || dis[j] < dis[id]) {
                    id = j;
                }
            }
            if (id == -1) {
                break;
            }
            use[id] = 1;
            for (int j = 0; j < n; j++) {
                if (dis[j] > max(dis[id], g[id][j])) {
                    dis[j] = max(dis[id], g[id][j]);
                }
            }
        }
        printf("Case #%d: %.20f\n", cas, dis[1]);
    }   
    return 0;
}