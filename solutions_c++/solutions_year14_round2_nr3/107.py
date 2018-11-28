#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>

#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <queue>
#include <stack>
#include <list>

#include <ctime>
#include <cassert>

using namespace std;

typedef long double ldb;
typedef long long int64;
typedef pair <int, int> pii;
typedef pair <double, double> pdd;

#define y0 wwwwwww
#define y1 qqqqqqq
#define next NEXT
#define prev PREV
#define forn(i, n) for (int i = 0; i < (int) n; i++)
#define ford(i, n) for (int i = (int) n - 1; i >= 0; i--)
#define seta(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define all(a) (a).begin(), (a).end()
#define last(a) a[a.size() - 1]
#define mp make_pair
#define fs first
#define sc second

template <class T> T sqr(T x) { return x * x; }

double const pi = 3.1415926535897932384626433832795;
int const inf = (int) 1e9;
int64 const inf64 = (int64) 4e18;

const int NMAX = 52;

vector<int> st;
int n, m, root, zn[NMAX];
int g[NMAX][NMAX], used2[NMAX], used[NMAX];
string ans;
char buf[10];

void dfs(int v) {
    used2[v] = 1;
    forn(i, n) {
        if (g[v][i] && !used[i] && !used2[i])
            dfs(i);
    }
}

int may(int w) {
    vector<int> good;
    ford(i, st.size()) {
        if (g[st[i]][w]) {
            forn(j, i + 1)
                good.pb(st[j]);
            break;
        }
    }
    seta(used2, 0);
    forn(i, good.size())
        dfs(good[i]);
    forn(i, n)
        if (!used[i] && !used2[i]) return 0;
    return 1;
}

void rec(int v) {
    st.pb(v);
    used[v] = 1;
    sprintf(buf, "%d", zn[v]);
    ans += (string) buf;

    vector<pii> now;
    forn(i, n)
        if (!used[i] && may(i))
            now.pb(mp(zn[i], i));
    if (now.size() > 0) {
        sort(all(now));
        while (!g[st.back()][now[0].sc])
            st.pop_back();
        rec(now[0].sc);
    }
    if (st.size() > 0 && st.back() == v) st.pop_back();
}

void solve() {
    root = 0;
    cin >> n >> m;
    forn(i, n) {
        scanf("%d", &zn[i]);
        if (zn[i] < zn[root])
            root = i;
    }
    seta(g, 0);
    forn(i, m) {
        int a, b;
        scanf("%d%d", &a, &b);
        a--, b--;
        g[a][b]++;
        g[b][a]++;
    }

    ans = "";
    seta(used, 0);
    rec(root);
    cout << ans << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    int tst;
    cin >> tst;
    forn(i, tst) {
        cerr << "----" << endl;
        cout << "Case #" << i + 1 << ": ";
        solve();
    }

	return 0;
}
