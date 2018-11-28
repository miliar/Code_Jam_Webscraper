#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }
using namespace std;

#define double long double

const int MN = 1000000;
double C, F, X, f[MN + 11];

double get(double X, double F, int k) {
    return X / (2.0 + k*F);
}

int main() {
    ios :: sync_with_stdio(false);
    cout << (fixed) << setprecision(7);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> C >> F >> X;
        double res = 1e100;
        FOR(k,0,MN) {
            if (k == 0) f[k] = 0;
            else f[k] = f[k-1] + get(C, F, k-1);

            res = min(res, f[k] + get(X, F, k));
        }
        cout << "Case #" << test << ": " << res << endl;
    }
    return 0;
}
