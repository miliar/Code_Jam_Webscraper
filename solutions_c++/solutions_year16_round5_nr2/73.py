#include <bits/stdc++.h>
using namespace std;
#define sz(x) ((int) (x).size())
#define forn(i,n) for (int i = 0; i < int(n); ++i)
typedef long long ll;
typedef long long i64;
typedef long double ld;
const int inf = int(1e9) + int(1e5);
const ll infl = ll(2e18) + ll(1e10);

const int maxn = 105;
vector<int> g[maxn];
int pr[maxn];
char s[maxn], ss[maxn];

ld C[maxn][maxn];

int cnt[maxn];
bool bad[maxn];
void pre(int u) {
    cnt[u] = 1;
    bad[u] = false;
    for (int v: g[u]) {
        pre(v);
        bad[v] = true;
        cnt[u] += cnt[v];
    }
}

int n;

ld P[maxn];

mt19937 rr(random_device{}());
ld rnd() {
    return ld(rr()) / rr.max();
}

void kill(int u) {
    bad[u] = true;
    for (int v: g[u])
        bad[v] = false;
}

void gen() {
    forn (iter, n + 1) {
        ld sum = 0;
        forn (i, n + 1) {
            if (bad[i]) {
                P[i] = 0;
                continue;
            }
            P[i] = cnt[i];
            sum += P[i];
        }
        //forn (i, n + 1)
            //cerr << P[i] << ' ';
        //cerr << '\n';
        forn (i, n + 1)
            P[i] /= sum;
        ld r = rnd();
        int u = 0;
        while (r > P[u]) {
            r -= P[u];
            ++u;
        }
        assert(!bad[u]);
        if (iter)
            ss[iter - 1] = s[u - 1];
        kill(u);
    }
}

const int buben = 1e4;
int test = 1;
void solve() {
    cin >> n;
    forn (i, n + 1)
        g[i].clear();
    forn (i, n) {
        int p;
        cin >> p;
        pr[i + 1] = p;
        g[p].push_back(i + 1);
    }
    int m;
    scanf("%s", s);
    cin >> m;
    vector<string> t;
    forn (i, m) {
        string qw;
        cin >> qw;
        t.push_back(qw);
    }
    vector<ld> res(m);
    forn (iter, buben) {
        pre(0);
        gen();
        ss[n] = 0;
        //cerr << ss << '\n';
        forn (i, m) {
            bool mt = false;
            forn (j, n - sz(t[i]) + 1) {
                bool ok = true;
                forn (k, sz(t[i]))
                    if (ss[j + k] != t[i][k])
                        ok = false, k = sz(t[i]);
                if (!ok)
                    continue;
                mt = true;
                break;
            }
            if (mt)
                ++res[i];
        }
    }
    cout << "Case #" << test++ << ":";
    forn (i, m)
        cout << ' ' << res[i] / buben;
    cout << '\n';
}

int main() {
    cout << fixed;
    cout.precision(4);
    #ifdef LOCAL
    assert(freopen("b.in", "r", stdin));
    #else
    #endif
    forn (i, maxn) {
        C[i][0] = C[i][i] = 1;
        for (int j = 1; j < i; ++j)
            C[i][j] = C[i - 1][j] + C[i - 1][j - 1];
    }
    int tn;
    cin >> tn;
    forn (i, tn)
        solve();
}
