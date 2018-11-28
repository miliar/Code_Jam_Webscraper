#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

struct node {
    int x1, y1, x2, y2;
};

const int N = 1010;
int dis[N][N], v[N], d[N];
node a[N];

int cal(int x1, int x2, int x3, int x4) {
    if (x1 > x4)
        return x1 - x4;
    else if (x2 < x3)
        return x3 - x2;
    else return 0;
}

void run(int cas) {
    int w, h, n;
    scanf("%d%d%d", &w, &h, &n);
    for (int i = 1; i <= n; i++) {
        scanf("%d%d%d%d", &a[i].x1, &a[i].y1, &a[i].x2, &a[i].y2);
        a[i].x2++;
        a[i].y2++;
    }
    memset(d, -1, sizeof(d));
    int t = n + 1;
    dis[0][t] = w;
    for (int i = 1; i <= n; i++) {
        dis[0][i] = a[i].x1;
        dis[i][t] = w - a[i].x2;
    }
    for (int i = 1; i <= n; i++)
        for (int j = i; j <= n; j++) {
            int dx = cal(a[i].x1, a[i].x2, a[j].x1, a[j].x2);
            int dy = cal(a[i].y1, a[i].y2, a[j].y1, a[j].y2);
            dis[i][j] = dis[j][i] = max(dx, dy);
        }
    memset(v, 0, sizeof(v));
    memset(d, -1, sizeof(d));
    d[0] = 0;
    for (int it = 0; it <= t; it++) {
        int ch = -1;
        for (int i = 0; i <= t; i++)
            if (!v[i] && d[i] != -1 && (ch == -1 || d[i] < d[ch]))
                ch = i;
        //printf("ch = %d, d[ch] = %d\n", ch, d[ch]);
        v[ch] = 1;
        for (int i = 1; i <= t; i++)
            if (d[i] == -1 || d[i] > d[ch] + dis[ch][i])
                d[i] = d[ch] + dis[ch][i];
        if (ch == t) break;
    }
    printf("Case #%d: %d\n", cas, d[t]);
}

int main() {
    int tt, cas;
    scanf("%d", &tt);
    for (cas = 1; cas <= tt; cas++)
        run(cas);
    return 0;
}

