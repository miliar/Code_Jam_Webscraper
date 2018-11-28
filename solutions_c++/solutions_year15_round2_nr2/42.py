
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

int m, n, k;

#define TWO(X) (1<<(X))
#define CONTAIN(S,X) (S & TWO(X))

int a[22][22];
int solve() {
    int res = 1000111000;
    REP(mask,TWO(m*n)) if (__builtin_popcount(mask) == k) {
        REP(i,m) REP(j,n) if (CONTAIN(mask, i*n+j)) {
            a[i][j] = 1;
        }
        else a[i][j] = 0;
        
        int cur = 0;
        REP(i,m) REP(j,n) if (a[i][j]) {
            if (j+1 < n && a[i][j+1]) ++cur;
            if (i+1 < m && a[i+1][j]) ++cur;
        }

        res = min(res, cur);
    }

    cout << m << ' ' << n << ' ' << k << endl;
    REP(mask,TWO(m*n)) if (__builtin_popcount(mask) == k) {
        REP(i,m) REP(j,n) if (CONTAIN(mask, i*n+j)) {
            a[i][j] = 1;
        }
        else a[i][j] = 0;
        
        int cur = 0;
        REP(i,m) REP(j,n) if (a[i][j]) {
            if (j+1 < n && a[i][j+1]) ++cur;
            if (i+1 < m && a[i+1][j]) ++cur;
        }

        if (cur == res) {
            REP(i,m) {
                REP(j,n) if (a[i][j]) cout << 'X'; else cout << '.';
                cout << endl;
            }
            cout << endl;
        }
    }
    return res;
}

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> m >> n >> k;
        printf("Case #%d: %d\n", test, solve());
    }
    return 0;
}

