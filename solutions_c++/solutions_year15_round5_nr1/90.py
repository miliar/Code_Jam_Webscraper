#include <cassert>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <string>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <queue>

using namespace std;

#define FOR(a, b) for (int a = 0; a < (b); ++a)
#define clr(a) memset(a, 0, sizeof(a))
#define pb(i) push_back(i)
#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)
#ifdef LOCAL
#define debug(a) cerr << #a << ": " << a << '\n';
#else
#define debug(a)
#endif

typedef long long ll;
typedef long double ldb;

const int INF = 1e9;
const ldb EPS = 1e-8;
const ldb PI = acos(-1.0);
const int MAXN = 1e6 + 100;

int s[MAXN];
int p[MAXN];
vector<int> c[MAXN];
int ord[MAXN];

bool _less(int a, int b) {
    return s[a] < s[b];
}

bool con[MAXN];
bool good[MAXN];

int cans;
int cnt = 0;
void adddfs(int v) {
    con[v] = true;
    cans++;
    for (auto u : c[v]) {
        //cnt++;
        if (!good[u])
            continue;
        adddfs(u);
    }
}
void add(int v) {
    good[v] = true;
    //debug(p[v]);
    if (v == 0 || con[p[v]]) {
        adddfs(v);
    }
}

void deldfs(int v) {
    con[v] = false;
    cans--;
    for (auto u : c[v]) {
        //cnt++;
        if (!good[u])
            continue;
        deldfs(u);
    }
}
void del(int v) {
    good[v] = false;
    if (con[v] == false)
        return;
    deldfs(v);
}
void read(int * a, int n) {
    int b, c, r;
    cin >> a[0] >> b >> c >> r;
    FOR(i, n - 1) {
        a[i + 1] = (a[i] * b + c) % r;
    }
}

int main() {
#ifdef LOCAL
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    //freopen("", "w", stderr);
#endif
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        debug(test);
        int n, d;
        cin >> n >> d;
        read(s, n);
        read(p, n);
        FOR(i, n) {
            c[i].clear();
            con[i] = false;
            good[i] = false;
        }
        for (int i = 1; i < n; ++i) {
            p[i] = p[i] % i;
            c[p[i]].pb(i);
        }
        FOR(i, n)
            ord[i] = i;
        sort(ord, ord + n, _less);
        int ans = 1;
        int st = 0, en = 0;
        cans = 0;
        while (st < n) {
            while (en < n && s[ord[en]] <= s[ord[st]] + d) {
                add(ord[en]);
                /*
                cerr << ord[en] << ' ' << cans << '\n';
                FOR(i, n) {
                    cerr << con[i] << ' ';
                }
                cerr << '\n';*/
                en++;
            }
            ans = max(ans, cans);
            del(ord[st]);
            st++;
        }
        printf("Case #%d: %d\n", test, ans);
    }
//    debug(cnt);
    return 0;
}

