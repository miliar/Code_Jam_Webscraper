#include <cstdio>
#include <algorithm>
#include <numeric>
#include <cstring>
#include <vector>
#include <stack>
#include <cmath>
using namespace std;

int x[1000], y[1000], z[1000];
int vx[1000], vy[1000], vz[1000];

double dissq(int i, int j, double t) {
    double dx = (x[i] + vx[i] * t) - (x[j] + vx[j] * t);
    double dy = (y[i] + vy[i] * t) - (y[j] + vy[j] * t);
    double dz = (z[i] + vz[i] * t) - (z[j] + vz[j] * t);
    return dx * dx + dy * dy + dz * dz;
}


struct Event {
    double time;
    int i, j;
    bool near;
} evnts[1000 * 1000 * 2];

int addevents(int i, int j, int loc, double d) {
    int dx = x[i] - x[j];
    int dy = y[i] - y[j];
    int dz = z[i] - z[j];
    int dvx = vx[i] - vx[j];
    int dvy = vy[i] - vy[j];
    int dvz = vz[i] - vz[j];
    if(dvx == 0 && dvy == 0 && dvz == 0) {
        if(dissq(i, j, 0.0) <= d) {
            evnts[loc++] = Event { -1, i, j, true };
        }
    }
    int a = dvx * dvx + dvy * dvy + dvz * dvz;
    int b = 2 * (dx * dvx + dy * dvy + dz * dvz);
    double c = dx * dx + dy * dy + dz * dz - d;
    double D = (long long) b * b - 4 * a * c;
    if(D > 0) {
        evnts[loc++] = Event{ (-b - sqrt(D)) / (2 * a), i, j, true };
        evnts[loc++] = Event{ (-b + sqrt(D)) / (2 * a), i, j, false };
    }
    return loc;
}

bool operator < (Event lhs, Event rhs) {
    return lhs.time < rhs.time;
}

bool near[1000][1000];
int adj[1000];
bool vis[1000];
double lastv[1000];

void dfs(int v, int n) {
    if(vis[v]) return;
    vis[v] = true;
    for(int i = 0; i < n; i++)
        if(near[v][i])
            dfs(i, n);
}

bool ok(int n, double d, int s) {
    int nevnts = 0;
    for(int i = 0; i < n; i++)
        for(int j = i + 1; j < n; j++)
            nevnts = addevents(i, j, nevnts, d);
    for(int i = 0; i < n; i++)
        fill_n(near[i], n, false);
    sort(evnts, evnts + nevnts);
    fill_n(vis, n, false);
    fill_n(adj, n, 0);
    int evi = 0;
    while(evi < nevnts && evnts[evi].time <= 0) {
        near[evnts[evi].i][evnts[evi].j] = evnts[evi].near;
        near[evnts[evi].j][evnts[evi].i] = evnts[evi].near;
        if(evnts[evi].near) {
            adj[evnts[evi].i]++;
            adj[evnts[evi].j]++;
        } else {
            adj[evnts[evi].i]--;
            adj[evnts[evi].j]--;
        }
        evi++;
    }

    dfs(0, n);

    if(vis[1]) return true;

    fill_n(lastv, n, 0);
    for(; evi < nevnts; evi++) {
        double tnow = evnts[evi].time;
        //XYZ(stderr, "> %f %d %d %d\n", tnow, evnts[evi].i, evnts[evi].j, evnts[evi].near ? 1 : 0);
        if(vis[evnts[evi].i] && adj[evnts[evi].i] == 0 && tnow - lastv[evnts[evi].i] > s) {
            vis[evnts[evi].i] = false;
            //XYZ(stderr, "YEEE\n");
        }
        if(vis[evnts[evi].j] && adj[evnts[evi].j] == 0 && tnow - lastv[evnts[evi].j] > s)
            vis[evnts[evi].j] = false;
        //XYZ(stderr, "> %d %d %f %d\n", vis[evnts[evi].i]+0, adj[evnts[evi].i], tnow - lastv[evnts[evi].i], s);


        near[evnts[evi].i][evnts[evi].j] = evnts[evi].near;
        near[evnts[evi].j][evnts[evi].i] = evnts[evi].near;
        if(evnts[evi].near) {
            adj[evnts[evi].i]++;
            adj[evnts[evi].j]++;
            if(vis[evnts[evi].i] && !vis[evnts[evi].j])
                dfs(evnts[evi].j, n);
            if(vis[evnts[evi].j] && !vis[evnts[evi].i])
                dfs(evnts[evi].i, n);
        } else {
            adj[evnts[evi].i]--;
            adj[evnts[evi].j]--;
            lastv[evnts[evi].i] = tnow;
            lastv[evnts[evi].j] = tnow;
        }
        if(vis[1]) return true;
    }

    return false;
}

double solve(int n, int s) {
    //XYZ(stderr, "$ %d\n", ok(n, 10.0, s) ? 1 : 0);
    // return 7122;

    double l = 0, r = dissq(0, 1, 0.0);
    for(int i = 0; i < 60; i++) {
        double m = (l + r) / 2;
        bool o = ok(n, m, s);
        // //XYZ(stderr, "%f %d\n", m, o ? 1 : 0);
        (o ? r : l) = m;
    }
    return sqrt((l + r) / 2);
}

int main() {
    int t;
    scanf("%d", &t);
    for(int tt = 1; tt <= t; tt++) {
        int n, s;
        scanf("%d %d", &n, &s);
        for(int i = 0; i < n; i++)
            scanf("%d%d%d%d%d%d", x + i, y + i, z + i, vx + i, vy + i, vz + i);
        printf("Case #%d: %.7f\n", tt, solve(n, s));
    }
}

