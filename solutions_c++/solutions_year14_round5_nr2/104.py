#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }
using namespace std;

int n, h[111], g[111], p, q;
int f[111][2011][2];
int res;

inline void update(int &x, int val) {
    x = max(x, val);
    res = max(res, val);
}

inline int get(int a, int b) {
    int res = a / b;
    if (a % b) ++res;
    return res;
}

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> p >> q >> n;
        FOR(i,1,n) cin >> h[i] >> g[i];

        REP(i,111) REP(j,2011) REP(k,2) f[i][j][k] = -1000111000;
        f[1][0][0] = 0;
        res = 0;

        FOR(i,1,n) FOR(save,0,2000) FOR(turn,0,1)
        if (f[i][save][turn] >= 0) {
            FOR(tower,0,15) {
                int qq = tower * q;

                // If we want to kill
                if (qq < h[i]) {
                    int need = get(h[i] - qq, p);
                    int has = save + tower - turn + 1;

                    if (has >= need
                            && (qq + (need-1)*p < h[i])) {
                        update(f[i+1][has-need][1], f[i][save][turn] + g[i]);
                    }
                }

                // If let tower kill
                if (qq >= h[i] && (qq-q < h[i])) {
                    update(f[i+1][save+tower-turn][0], f[i][save][turn]);
                }
            }
        }

        cout << "Case #" << test << ": " << res << endl;
        cerr << test << endl;
    }
    return 0;
}
