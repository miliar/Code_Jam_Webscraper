
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

int m, n;
char a[111][111];

bool isBad(int u, int v) {
    FOR(i,1,m) if (i != u && a[i][v] != '.') return false;
    FOR(j,1,n) if (j != v && a[u][j] != '.') return false;
    return true;
}

bool bad() {
    FOR(i,1,m) FOR(j,1,n)
        if (a[i][j] != '.' && isBad(i, j)) return true;
    return false;
}

int count() {
    int cnt = 0;
    FOR(i,1,m) FOR(j,1,n) if (a[i][j] != '.') {
        int u = i, v = j;
        while (true) {
            if (a[i][j] == '^') --u;
            else if (a[i][j] == 'v') ++u;
            else if (a[i][j] == '<') --v;
            else if (a[i][j] == '>') ++v;
            else cout << ":@)" << endl;

            if (u == 0 || v == 0 || u > m || v > n) {
                ++cnt;
                break;
            }
            if (a[u][v] != '.') break;
        }
    }
    return cnt;
}

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> m >> n;
        FOR(i,1,m) FOR(j,1,n) cin >> a[i][j];

        cout << "Case #" << test << ": ";
        if (bad()) cout << "IMPOSSIBLE" << endl;
        else cout << count() << endl;
    }
    return 0;
}

