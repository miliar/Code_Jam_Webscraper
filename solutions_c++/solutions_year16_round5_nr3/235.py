#include <bits/stdc++.h>
using namespace std;
const int maxn = 1005;
const double eps = 1e-4;

bool vis[maxn];
int n, s;
int x[maxn], y[maxn], z[maxn], vx[maxn], vy[maxn], vz[maxn];
double r, jump[maxn][maxn][2], mn[maxn];
vector<pair<double, double> > cur;

double dist(double a, double b, double c) {
    return sqrt(a * a + b * b + c * c);
}

pair<double, double> go(double a, double b, double c, double u, double v, double w) {
    double lo = -3e3, hi = 3e3;
    for (int i = 0; i < 30; i++) {
        double mid = (lo + hi) / 2;
        if (dist(a + mid * u, b + mid * v, c + mid * w) 
                > dist(a + mid * u + eps * u, 
                       b + mid * v + eps * v, 
                       c + mid * w + eps * w) ) {
            lo = mid;
        } else {
            hi = mid;
        }
    }

    double center = lo;
    if (dist(a + center * u, 
             b + center * v, 
             c + center * w) > r) {
        return {-1, -1};
    }

    lo = 0, hi = 3e3;
    for (int i = 0; i < 30; i++) {
        double mid = (lo + hi) / 2;
        if (dist(a + mid * u + center * u, 
                 b + mid * v + center * v, 
                 c + mid * w + center * w) < r) {
            lo = mid;
        } else {
            hi = mid;
        }
    }

    return {center - lo, center + lo};
}

bool check() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            x[j] -= x[i];
            y[j] -= y[i];
            z[j] -= z[i];
            vx[j] -= vx[i];
            vy[j] -= vy[i];
            vz[j] -= vz[i];

            if (vx[j] == 0 && vy[j] == 0 && vz[j] == 0) {
                if (sqrt(x[j] * x[j] + y[j] * y[j] + z[j] * z[j]) < r) {
                    jump[i][j][0] = 0;
                    jump[i][j][1] = numeric_limits<double>::infinity();
                } else {
                    jump[i][j][0] = jump[i][j][1] = -1;
                }
            } else {
                auto ret = go(x[j], y[j], z[j], vx[j], vy[j], vz[j]);
                jump[i][j][0] = ret.first;
                jump[i][j][1] = ret.second;
            }

            jump[j][i][0] = jump[i][j][0];
            jump[j][i][1] = jump[i][j][1];

            x[j] += x[i];
            y[j] += y[i];
            z[j] += z[i];
            vx[j] += vx[i];
            vy[j] += vy[i];
            vz[j] += vz[i];
        }
    }

    /*for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << i << ' ' << j << ' ' << jump[i][j][0] << ' ' << jump[i][j][1] << '\n';
        }
    }*/

    memset(vis, 0, sizeof(vis));
    fill_n(mn, maxn, numeric_limits<double>::infinity());
    mn[0] = 0;
    priority_queue<pair<double, int> > pq;
    pq.push({0.0, 0});
    while (!pq.empty()) {
        auto process = pq.top();
        pq.pop();

        int u = process.second;
        if (u == 1) {
            return true;
        }
        if (vis[u]) {
            continue;
        }
        vis[u] = true;
        double b = process.first;
        double e = b + s;

        cur.clear();
        for (int i = 0; i < n; i++) {
            if (i != u) {
                cur.push_back({jump[u][i][0], jump[u][i][1]});
            }
        }
        sort(cur.begin(), cur.end());

        for (auto rng : cur) {
            if (rng.first - eps <= e && b - eps <= rng.second) {
                e = max(rng.second, e) + s;
            }
        }
        for (int i = 0; i < n; i++) {
            if (i != u) {
                if (jump[u][i][0] - eps <= e && b - eps <= jump[u][i][1]) {
                    double arrive = max(b, jump[u][i][0]);
                    if (arrive < mn[i]) {
                        mn[i] = arrive;
                        pq.push({mn[i], i});
                    }
                }
            }
        }
    }
    return false;
}

void solve() {
    cin >> n >> s;
    for (int i = 0; i < n; i++) {
        cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
    }

    double lo = 0, hi = 3e3;
    for (int i = 0; i < 30; i++) {
        double mid = (lo + hi) / 2;
        r = mid;
        if (check()) {
            hi = mid;
        } else {
            lo = mid;
        }
    }
    cout << lo;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout << fixed << setprecision(9);
    int numCases;
    cin >> numCases;
    for (int i = 1; i <= numCases; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << '\n';
    }
    return 0;
}
