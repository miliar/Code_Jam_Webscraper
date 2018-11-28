#include <bits/stdc++.h>

using namespace std;

#define FOR(i, a, b) for(int i = a; i <= b; i++)
#define REP(i, a, b) for(int i = a; i >= b; i--)
#define sz(x) (int)x.size()
#define pb push_back
#define mp make_pair

typedef pair<int, int> II;
typedef long long ll;

const int inf = (int)(1e9);
const int Nmax = 111;

int a[Nmax][Nmax], f[Nmax][Nmax][5], n, m, d[Nmax][Nmax], c[Nmax][Nmax], dd[1111], res;

void solve() {
    memset(f, 0, sizeof f);
    memset(d, 0, sizeof d);
    memset(c, 0, sizeof c);
    FOR(i, 1, m) FOR(j, 1, n) {
        d[i][j] = d[i - 1][j] + (int)(a[i][j] != 4);
        c[i][j] = c[i][j - 1] + (int)(a[i][j] != 4);
        if (c[i][j - 1] == 0) f[i][j][0] = 1;
        if (d[i - 1][j] == 0) f[i][j][1] = 1;
    }
    REP(i, m, 1) REP(j, n, 1) {
        d[i][j] = d[i + 1][j] + (int)(a[i][j] != 4);
        c[i][j] = c[i][j + 1] + (int)(a[i][j] != 4);
        if (c[i][j + 1] == 0) f[i][j][2] = 1;
        if (d[i + 1][j] == 0) f[i][j][3] = 1;
    }
    //FOR(i, 1, m) FOR(j, 1, n)  FOR(k, 0, 3) cout << f[i][j][k] << endl;
    res = 0;
    FOR(i, 1, m) FOR(j, 1, n) if (a[i][j] != 4) {
        int k = a[i][j];
        if (f[i][j][k]) {
            res++;
            int ok = 0;
            FOR(t, 0, 3) if (f[i][j][t] == 0) ok = 1;
            if (ok == 0) {
                res = -1;
                return;
            }
        }
    }
}

int main() {
   // freopen("A-large.in", "r", stdin);
   // freopen("ans.out", "w", stdout);
    dd['<'] = 0;
    dd['^'] = 1;
    dd['>'] = 2;
    dd['v'] = 3;
    dd['.'] = 4;
    int test;
    cin >> test;
    FOR(t, 1, test) {
        cin >> m >> n;
        FOR(i, 1, m){
            string s;
            cin >> s;
            FOR(j, 1, n)
                a[i][j] = dd[s[j - 1]];
        }
        solve();
        cout << "Case #" << t << ": ";
        if (res == -1) cout << "IMPOSSIBLE" << endl;
        else cout << res << endl;
    }
    return 0;
}

