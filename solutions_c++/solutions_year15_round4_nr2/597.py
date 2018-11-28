#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
#include <iomanip>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i)
typedef long long LL;

#define EPS 1e-12

int N;
double V, X;

void run() {
    cin >> N >> V >> X;
    vector<pair<double, double> > mm;
    REP(i, N) {
        double R, C;
        cin >> R >> C;
        mm.push_back(make_pair(R, C));
    }
    if (N == 1) {
        if (fabs(X - mm[0].second) > EPS) cout << "IMPOSSIBLE" << endl;
        else cout << setprecision(10) << fixed << V / mm[0].first << endl;
    }
    if (N == 2) {
        double r1 = mm[0].first, r2 = mm[1].first;
        double c1 = mm[0].second, c2 = mm[1].second;
        if (fabs(X - c1) < EPS && fabs(X - c2) < EPS) {
            double res = V / (r1 + r2);
            cout << setprecision(10) << fixed << res << endl;
            return;
        }
        if (fabs(X - c1) < EPS) {
            cout << setprecision(10) << fixed << V / r1 << endl;
            return;
        }
        if (fabs(X - c2) < EPS) {
            cout << setprecision(10) << fixed << V / r2 << endl;
            return;
        }
        if ((c1 > X && c2 > X) || (c1 < X && c2 < X)) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }

        double v1 = V * (X - c2) / (c1 - c2), v2 = V - v1;
        double res = max(v1 / r1, v2 / r2);
        cout << setprecision(10) << fixed << res << endl;
    }
}

int main() {
    int k;
    cin >> k;
    FOR(c,1,k) {
        cout << "Case #" << c << ": ";
        run();
    }
    return 0;
}
