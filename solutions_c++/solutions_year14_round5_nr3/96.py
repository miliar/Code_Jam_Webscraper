#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }
using namespace std;

#define TWO(x) (1<<(x))
#define CONTAIN(S,x) (S & TWO(x))
;

int n;
pair<char,int> a[22];
bool f[20][TWO(16)];

bool check() {
    FOR(j,1,n) FOR(i,1,j-1) if (a[i].second == a[j].second && a[i].second) {
        if (a[i].first == a[j].first) {
            bool ok = false;
            FOR(k,i+1,j-1) {
                if (a[k].second == 0 && a[k].first != a[i].first) {
                    a[k].second = a[i].second;
                    ok = true;
                    break;
                }
            }
            if (!ok) {
                return false;
            }
        }
        else break;
    }
    return true;
}

bool can(int x, int y) {
    return x == y || !(x * y);
}

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> n;
        FOR(i,1,n) cin >> a[i].first >> a[i].second;

        cout << "Case #" << test << ": ";
        if (!check()) {
            cout << "CRIME TIME" << endl;
            continue;
        }

        memset(f, false, sizeof f);
        f[0][0] = true;
        FOR(i,0,n-1) REP(mask,TWO(n))
        if (f[i][mask]) {
            if (a[i+1].first == 'E') {
                f[i+1][mask | TWO(i)] = true;
            }
            else {
                f[i+1][mask] = true;
                REP(j,n)
                if (CONTAIN(mask,j) && can(a[j+1].second, a[i+1].second)) {
                    f[i+1][mask - TWO(j)] = true;
                }
            }
        }

        bool ok = false;
        int res = n + 1;
        REP(mask,TWO(n)) {
            if (f[n][mask]) res = min(res, __builtin_popcount(mask));
        }

        if (res > n) cout << "CRIME TIME" << endl;
        else cout << res << endl;
    }
    return 0;
}
