#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define EACH(it,a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); ++it)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }

#define sqr(x) ((x) * (x))
using namespace std;

int n;
double c[111], r[111];
double V, X;

int cmp(double a, double b) {
    if (fabs(a - b) < 1e-6) return 0;
    if (a < b) return -1;
    return 1;
}

int main() {
    ios :: sync_with_stdio(false);
    cout << (fixed) << setprecision(9);

    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> n >> V >> X;
        FOR(i,1,n) cin >> r[i] >> c[i];

        if (n == 2) {
            if (cmp(c[1], c[2]) == 0) {
                n = 1;
                r[1] = r[1] + r[2];
            }
        }

        cout << "Case #" << test << ": ";
        if (n == 1) {
            if (cmp(c[1], X) == 0) cout << V / r[1] << endl;
            else cout << "IMPOSSIBLE" << endl;
        }
        else {
            if (cmp(c[1], X) == 0) cout << V / r[1] << endl;
            else if (cmp(c[2], X) == 0) cout << V / r[2] << endl;
            else {
                double t2 = (X*V - c[1]*V) / r[2] / (c[2] - c[1]);
                double t1 = (X*V - c[2]*V) / r[1] / (c[1] - c[2]);

                if (t1 < 0 || t2 < 0) cout << "IMPOSSIBLE" << endl;
                else {
                    cout << max(t1, t2) << endl;
                    assert(t1 >= 0);
                    assert(t2 >= 0);
                    assert(cmp(t1 * r[1] + t2 * r[2], V) == 0);
                    assert(cmp((t1*r[1] * c[1] + t2*r[2] * c[2]) / V, X) == 0);
                }
            }
        }
    }
    return 0;
}

