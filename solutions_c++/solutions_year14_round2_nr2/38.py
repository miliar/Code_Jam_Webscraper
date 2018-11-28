#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }
using namespace std;

int a, b, k;
int ba[33], bb[33], bk[33];
long long f[33][2][2][2];

void init() {
    memset(f, 0, sizeof f);

    REP(i,31) {
        ba[30-i] = (a >> i) & 1;
        bb[30-i] = (b >> i) & 1;
        bk[30-i] = (k >> i) & 1;
    }
    // PR0(ba, 31);
}

long long solve() {
    f[0][0][0][0] = 1;
    FOR(i,0,29) REP(la,2) REP(lb,2) REP(lk,2) if (f[i][la][lb][lk]) {
        REP(cura,2) REP(curb,2) {
            int curk = cura & curb;

            if (!la && cura > ba[i+1]) continue;
            if (!lb && curb > bb[i+1]) continue;
            if (!lk && curk > bk[i+1]) continue;

            int na = la, nb = lb, nk = lk;
            if (cura < ba[i+1]) na = 1;
            if (curb < bb[i+1]) nb = 1;
            if (curk < bk[i+1]) nk = 1;

            f[i+1][na][nb][nk] += f[i][la][lb][lk];
        }
    }
    return f[30][1][1][1];
}

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> a >> b >> k;
        init();
        long long res = solve();
        cout << "Case #" << test << ": " << res << "\n";
    }
    return 0;
}
