#include <bits/stdc++.h>

using namespace std;

#define x first
#define y second
#define INF (0x3f3f3f3f)

#define SZ(x) ((int)((x).size()))
#define PB(x) push_back(x)
#define MEMSET(x,v) memset(x,v,sizeof(x))
#define REP(i,n) for(int (i)=0;(i)<(n);++(i))

typedef long long LL;
typedef pair<int, int> PII; typedef pair<PII, int> PII2;

#define MAXN (105)

const double EPS = 1e-12;

int N;
double V, X;
double rate[MAXN];
double temp[MAXN];

double cal_temp(double v1, double v2, double x1, double x2) {
    return (v1 * x1 + v2 * x2) / (v1 + v2);
}

bool good(double t) {
    REP(i, N) {
        if (abs(temp[i] - X) < EPS) {
            if (rate[i] * t >= V - EPS) {
                return true;
            }
        }
    }
    REP(i, N) {
        REP(j, N) {
            if (i == j) continue;
            if (temp[i] <= X && temp[j] >= X) {
                double v1 = rate[i] * t;
                double v2 = rate[j] * t;
                if (v1 + v2 < V + EPS) continue;

                double maxt = -1.0;
                double mint = 105.0;
                // v1 = 0
                if (v2 >= V - EPS) {
                    mint = min(mint, cal_temp(0, V, temp[i], temp[j]));
                    maxt = max(maxt, cal_temp(0, V, temp[i], temp[j]));
                }
                // v2 = 0
                if (v1 >= V - EPS) {
                    mint = min(mint, cal_temp(V, 0, temp[i], temp[j]));
                    maxt = max(maxt, cal_temp(V, 0, temp[i], temp[j]));
                }
                // v1 = min(V, v1);
                {
                    double vv = min(V, v1);
                    mint = min(mint, cal_temp(vv, V - vv, temp[i], temp[j]));
                    maxt = max(maxt, cal_temp(vv, V - vv, temp[i], temp[j]));
                }
                {
                    double vv = min(V, v2);
                    mint = min(mint, cal_temp(V - vv, vv, temp[i], temp[j]));
                    maxt = max(maxt, cal_temp(V - vv, vv, temp[i], temp[j]));
                }
                if (X >= mint - EPS && X <= maxt + EPS) {
                    return true;
                }
            }
        }
    }
    return false;
}

void solve() {
    cin >> N >> V >> X;
    REP(i, N) {
        cin >> rate[i] >> temp[i];
    }
    double best_t = -1.0;

    double left = 0.0, right = 1000000000000.0;
    REP(iter, 300) {
        double mid = (left + right) / 2;
        if (good(mid)) {
            if (best_t < -0.5 || best_t > mid) best_t = mid;
            right = mid;
        } else {
            left = mid;
        }
    }
    if (best_t < -0.5) {
        printf("IMPOSSIBLE\n");
    } else {
        printf("%.9lf\n", best_t);
    }
}

int main() {
    int T;
    cin >> T;
    REP(t, T) {
        printf("Case #%d: ", t + 1);
        solve();
    }


    return 0;
}
