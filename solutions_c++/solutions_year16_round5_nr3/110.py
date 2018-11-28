#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
using namespace std;

struct point {
    double x, y, z;
};

double dist(point a, point b) {
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y) + (a.z - b.z) * (a.z - b.z));
}

struct el {
    int a, b;
    double di;
    bool operator<(const el &e) const {
        return di < e.di;
    }
};

int par[1024];

int ufind(int v) {
    if (par[v] == -1) {
        return v;
    }
    return (par[v] = ufind(par[v]));
}

int n, s;
point p[1024];
vector<el> ve;

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        memset(par, -1, sizeof(par));
        scanf("%d %d", &n, &s);
        for (int i = 0; i < n; ++i) {
            scanf("%lf %lf %lf", &p[i].x, &p[i].y, &p[i].z);
            scanf("%lf %lf %lf", &p[n].x, &p[n].y, &p[n].z);
        }
        ve.clear();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (i == j) {
                    continue;
                }
                el e;
                e.a = i;
                e.b = j;
                e.di = dist(p[i], p[j]);
                ve.push_back(e);
            }
        }
        sort(ve.begin(), ve.end());
        double ans = 0;
        for (int i = 0; i < (int) ve.size(); ++i) {
            int v = ve[i].a;
            int u = ve[i].b;
            if (ufind(v) == ufind(u)) {
                continue;
            }
            par[ufind(v)] = ufind(u);
            if (ufind(0) == ufind(1)) {
                ans = ve[i].di;
                break;
            }
        }
        printf("Case #%d: %.10lf\n", t, ans);
    }
    return 0;
}
