#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)
typedef long long LL;
typedef pair<int, int> PII;

int tt;
int n, s;
int x[1000], y[1000], z[1000], vx[1000], vy[1000], vz[1000];
bool used[1000];
int dist[1000][1000];

int mid;

void dfs(int v) {
    used[v] = true;
    REP(i, n) if (!used[i] && dist[v][i] <= mid) {
        dfs(i);
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &tt);
    for (int test = 1; test <= tt; ++test) {
        printf("Case #%d: ", test);
        scanf("%d%d", &n, &s);
        REP(i, n) {
            scanf("%d%d%d%d%d%d", x + i, y + i, z + i, vx + i, vy + i, vz + i);
        }
        REP(i, n) REP(j, n) {
            int dx = x[i] - x[j];
            int dy = y[i] - y[j];
            int dz = z[i] - z[j];
            dist[i][j] = dx * dx + dy * dy + dz * dz;
        }
        int lo = 0, hi = 3000005;
        while (lo < hi) {
            mid = (lo + hi) >> 1;
            REP(i, n) used[i] = false;
            dfs(0);
            if (used[1]) hi = mid;
            else lo = mid + 1;
        }
        printf("%.12f\n", sqrt((double)lo));
        cerr << "done " << test << endl;
    }
    return 0;
}
