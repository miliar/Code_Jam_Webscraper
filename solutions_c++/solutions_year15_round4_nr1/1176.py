#include <bits/stdc++.h>
using namespace std;

#define fr(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define frr(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define rep(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define repr(i,n) for (int i = (n) - 1; i >= 0; i--)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))

#define uint64 unsigned long long
#define int64 long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define PI  3.1415926535897932385
#define EPS 1e-7
#define MOD 1000000007
#define INF 1500111222
#define MAX 111

const int dx[] = { 1, -1, 0, 0 };
const int dy[] = { 0, 0, -1, 1 };
int n, m;
char s[MAX][MAX];

bool inside(int x, int y) { return 0 <= x && x < n && 0 <= y && y < m; }

bool canChange(int x, int y) {
    rep(k, 4) {
        int i = x, j = y;
        while (true) {
            i += dx[k];
            j += dy[k];
            if (!inside(i, j)) break;
            if (s[i][j] != '.') return true;
        }
    }
    return false;
}

ii lookUp(int x, int y, int dir, char value) {
    while (inside(x, y)) {
        if (s[x][y] != '.') {
            if (s[x][y] == value)
                return mp(x, y);
            return mp(-1, -1);
        }
        x += dx[dir];
        y += dy[dir];
    }
    return mp(-1, -1);
}

int solve() {
    vii list;
    rep(i, n) {
        ii p1 = lookUp(i, 0, 3, '<');
        ii p2 = lookUp(i, m - 1, 2, '>');
        if (p1.ff != -1) list.pb(p1);
        if (p2.ff != -1) list.pb(p2);
    }
    rep(j, m) {
        ii p1 = lookUp(0, j, 0, '^');
        ii p2 = lookUp(n - 1, j, 1, 'v');
        if (p1.ff != -1) list.pb(p1);
        if (p2.ff != -1) list.pb(p2);
    }
    //rep(i, list.size())
    //    printf("%d %d: %c\n", list[i].ff, list[i].ss, s[list[i].ff][list[i].ss]);

    rep(i, list.size())
        if (!canChange(list[i].ff, list[i].ss))
            return -1;
    return list.size();
}

int main() {
    #ifndef ONLINE_JUDGE
        freopen("alarge.inp", "r", stdin);
        freopen("alarge.out", "w", stdout);
    #endif
    int cases, caseNo = 0;
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d %d", &n, &m);
        rep(i, n) scanf(" %s ", s[i]);
        printf("Case #%d: ", ++caseNo);
        int res = solve();
        if (res >= 0) printf("%d\n", res);
        else puts("IMPOSSIBLE");
    }
    return 0;
}

// Viet P. Lam - lamphanviet@gmail.com - http://blog.lamphanviet.com