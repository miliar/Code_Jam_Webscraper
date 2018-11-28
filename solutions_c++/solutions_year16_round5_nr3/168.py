#include "bits/stdc++.h"
#define puba push_back
#define mapa make_pair
#define ff first
#define ss second
#define bend(_x) (_x).begin(), (_x).end()
#define szof(_x) ((int) (_x).size())
#define TASK_NAME ""

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const double INF = 1e100;
const int MAXN = 1000;

struct point {
    double x, y, z;
    point() {
        x = y = z = 0;
    }
    point(int _x, int _y, int _z) {
        x = _x;
        y = _y;
        z = _z;
    }
};

double dist[MAXN];

double get_dist(point p1, point p2) {
    double x = p1.x - p2.x;
    double y = p1.y - p2.y;
    double z = p1.z - p2.z;
    return sqrt(x * x + y * y + z * z);
}

int solve() {
    int n, s;
    scanf("%d%d", &n, &s);

    vector<point> coords, speed;

    for (int i = 0; i < n; ++i) {
        int x, y, z;
        scanf("%d%d%d", &x, &y, &z);
        coords.puba(point(x, y, z));
        scanf("%d%d%d", &x, &y, &z);
        speed.puba(point(x, y, z));
    }

    for (int i = 0; i < n; ++i) {
        dist[i] = INF;
    }

    set<pair<double, int>> q;
    q.insert({0, 0});

    while (szof(q)) {
        pair<double, int> p = *q.begin();
        q.erase(q.begin());
        if (p.ss == 1) {
            printf("%.20f\n", p.ff);
            return 0;
        }
        for (int i = 0; i < n; ++i) {
            if (dist[i] > max(p.ff, get_dist(coords[i], coords[p.ss]))) {
                q.erase({dist[i], i});
                dist[i] = max(p.ff, get_dist(coords[i], coords[p.ss]));
                q.insert({dist[i], i});
            }
        }
    }

    /*
    double l = 0, r = 10000;
    for (int i = 0; i < 100; ++i) {
        double mid = (l + r) / 2;

        for (int j = 0; j < n; ++j) {
            dist[j] = INF;
        }

        bool flag = false;
        set<pair<double, int>> q;
        q.insert({0, 0});
        dist[0] = 0;
        while (szof(q)) {
            pii p = q.p
        }
    }*/
    
    return 0;
}

int main() {
    //freopen(TASK_NAME ".in", "r", stdin);
    //freopen(TASK_NAME ".out", "w", stdout);

    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }

    return 0;
}