#ifdef NALP_PROJECT
#pragma hdrstop
#else
#define _SECURE_SCL 0
#endif

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:200000000")

#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <utility>
#include <cassert>

#include <set>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <bitset>
#include <memory.h>

#include <iostream>
#include <fstream>
#include <sstream>

#ifdef _WIN32
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

using namespace std;

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define y1 YYY1
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

template<typename T> inline T Abs(T x) { return (x >= 0) ? x : -x; }
template<typename T> inline T sqr(T x) { return x * x; }
template<typename T> inline string toStr(T x) { stringstream st; st << x; string s; st >> s; return s; }
template<typename T> inline int bit(T mask, int b) { return (b >= 0 && (mask & (T(1) << b)) != 0) ? 1 : 0; }

inline int nextInt() { int x; if (scanf("%d", &x) != 1) throw; return x; }
inline int64 nextInt64() { int64 x; if (scanf(LLD, &x) != 1) throw; return x; }
inline double nextDouble() { double x; if (scanf("%lf", &x) != 1) throw; return x; }

const int INF = (int)1E9;
const int64 INF64 = (int64)1E18;
const long double EPS = 1E-9;
const long double PI = 3.1415926535897932384626433832795;

const int MAXN = 2000100;
const int OSN = (1 << 21) - 1;

int n, l[MAXN], c[MAXN], pre[MAXN], lz[MAXN], rz[MAXN], upd[2*OSN + 1000];
int64 D, S0, As, Cs, Rs, M0, Am, Cm, Rm;
pair<int, int> tree[2*OSN + 1000];
int64 S[MAXN], M[MAXN];
vector<int> g[MAXN];
vector<int> st;

void push(int v, int l, int r) {
    tree[v].first += upd[v];
    if (l != r) {
        upd[2*v + 1] += upd[v];
        upd[2*v + 2] += upd[v];
    }
    upd[v] = 0;
}

pair<int, int> f(const pair<int, int>& a, const pair<int, int>& b) {
    if (a.first < b.first) return a;
    if (a.first > b.first) return b;
    return mp(a.first, a.second + b.second);
}

void update(int v, int l, int r, int ll, int rr, int value) {
    push(v, l, r);
    if (l > rr || ll > r || ll > rr) return;
    if (ll <= l && r <= rr) {
        upd[v] += value;
        push(v, l, r);
        return;
    }

    int mid = (l + r) >> 1;
    update(2*v + 1, l, mid, ll, rr, value);
    update(2*v + 2, mid + 1, r, ll, rr, value);
    tree[v] = f(tree[2*v + 1], tree[2*v + 2]);
}

void init(int v, int l, int r) {
    if (l == r) {
        tree[v] = mp(0, 1);
        return;
    }

    int mid = (l + r) >> 1;
    init(2*v + 1, l, mid);
    init(2*v + 2, mid + 1, r);
    tree[v] = f(tree[2*v + 1], tree[2*v + 2]);
}

void DFS(int v) {
    lz[v] = int(st.size());
    st.push_back(v);
    forn(i, g[v].size()) {
        DFS(g[v][i]);
    }
    rz[v] = int(st.size()) - 1;
}

int leader(int v) {
    if (v != l[v]) l[v] = leader(l[v]);
    return l[v];
}

int solve(int64 lf, int64 rg) {
    if (S[0] > rg || S[0] < lf) {
        return 0;
    }

    forn(i, n) {
        l[i] = i;
        c[i] = 1;
    }

    forn(v, n) {
        if (lf <= S[v] && S[v] <= rg) {
            int u = leader(pre[v]);
            if (u != v) {
                c[u] += c[v];
                l[v] = u;
                c[v] = 0;
            }
        }
    }

    return c[0];
}

int stupid() {
    int ans = 0;
    forn(st, n) {
        int64 lf = S[st];
        ans = max(ans, solve(lf, lf + D));
    }
    return ans;
}

void solve(bool skipThisTest) {
    if (true) {
        cerr << "\tinput mode: read test." << endl;
        n = nextInt();
        D = nextInt();
        S0 = nextInt();
        As = nextInt();
        Cs = nextInt();
        Rs = nextInt();
        M0 = nextInt();
        Am = nextInt();
        Cm = nextInt();
        Rm = nextInt();
        if (skipThisTest) return;
    } else {
        n = 1000;
        D = rand() % 100000;
        S0 = rand() % 100000;
        As = rand() % 100000;
        Cs = rand() % 100000;
        Rs = rand() % 100000;
        M0 = rand() % 100000;
        Am = rand() % 100000;
        Cm = rand() % 100000;
        Rm = rand() % 100000;
        cerr << "\tinput mode: generated test." << endl;
        // generate test.
    }

    st.clear();
    forn(i, n) {
        g[i].clear();
    }

    pre[0] = 0;
    S[0] = S0;
    M[0] = M0;
    for (int i = 1; i < n; ++i) {
        S[i] = (S[i - 1] * As + Cs) % Rs;
        M[i] = (M[i - 1] * Am + Cm) % Rm;
        pre[i] = int(M[i] % i);
        g[pre[i]].pb(i);
    }

    DFS(0);
    memset(upd, 0, sizeof upd);
    init(0, 0, OSN);

    update(0, 0, OSN, n, OSN, +100);
    forn(i, n) {
        update(0, 0, OSN, lz[i], rz[i], +1);
    }

    vector<pair<int64, int> > l;
    forn(i, n) {
        l.pb(mp(S[i], i));
    }

    int ans = 0, r = 0;
    sort(all(l));
    forn(i, n) {
        while (r < n && l[r].first - l[i].first <= D) {
            int u = l[r].second;
            update(0, 0, OSN, lz[u], rz[u], -1);
            r++;
        }

        if (tree[0].first == 0) {
            ans = max(ans, tree[0].second);
        }

        int v = l[i].second;
        update(0, 0, OSN, lz[v], rz[v], +1);
    }

    cout << ans << endl;

    cerr << "\tclever answer is '" << ans << "'." << endl;
    if (n <= 1000) {
        int stupidAnswer = stupid();
        cerr << "\tstupid answer is '" << stupidAnswer << "'." << endl;
        assert(ans == stupidAnswer);
    }
}

int main(int argc, char * argv[]) {
#ifdef NALP_PROJECT
    freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
#else
#endif

    int minTest = 1, maxTest = INF;
    if (argc == 3) {
        minTest = atoi(argv[1]);
        maxTest = atoi(argv[2]);
    }

    cout.precision(10);
    cout.setf(ios::fixed);

    cerr.precision(10);
    cerr.setf(ios::fixed);

    srand((unsigned int)time(0));
    int tests = nextInt();
    clock_t totalStartTime = clock();
    for(int test = 1; test <= tests; test++) {
        clock_t startTime = clock();
        cerr << "Case #" << test << endl;
        bool skipThisTest = (test < minTest || test > maxTest);
        if (!skipThisTest) cout << "Case #" << test << ": ";
        solve(skipThisTest);

        char formattedTime[100];
        clock_t time = clock() - startTime;
        sprintf(formattedTime, "%d.%03d", int(time / CLOCKS_PER_SEC), int(time % CLOCKS_PER_SEC));
        cerr << "time for test is " << formattedTime << " s." << endl << endl;
    }

    char formattedTime[100];
    clock_t totalTime = clock() - totalStartTime;
    sprintf(formattedTime, "%d.%03d", int(totalTime / CLOCKS_PER_SEC), int(totalTime % CLOCKS_PER_SEC));
    cerr << string(20, '=') << endl;
    cerr << "TOTAL TIME IS " << formattedTime << " s." << endl;

    return 0;
}
