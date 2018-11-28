#include <bits/stdc++.h>

#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define for1(i, n) for(int i = 1; i <= (int)(n); i++)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define prev asdfsdf
#define x first
#define y second

using namespace std;
typedef long double ld;
typedef long long ll;
typedef pair<int, int> PII;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef long long i64;
typedef unsigned long long ull;

template<class T>
bool remin(T &a, const T &b) {
    if (a > b) {
        a = b;
        return true;
    }
    return false;
}

template<class T>
bool remax(T &a, const T &b) {
    if (a < b) {
        a = b;
        return true;
    }
    return false;
}

int nxt() {
    int x;
    scanf("%d", &x);
    return x;
}

ll gcd(ll a, ll b) {
    a = abs(a);
    b = abs(b);
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

typedef ld ptdata;

struct pt {
    ptdata x, y;

    pt() { }

    pt(ptdata x, ptdata y) : x(x), y(y) { }

    pt operator-(const pt &r) const {
        return pt(x - r.x, y - r.y);
    }

    pt operator+(const pt &r) const {
        return pt(x + r.x, y + r.y);
    }

    pt operator*(const ld &r) const {
        return pt(x * r, y * r);
    }

    ptdata sqlen() const {
        return abs(x * x + y * y);
    }

    ld len() const {
        return sqrtl(sqlen());
    }

    bool operator<(const pt &r) const {
        if (x != r.x) return x < r.x;
        return y < r.y;
    }

    bool operator==(const pt &r) const {
        return x == r.x && y == r.y;
    }
};

ptdata cross(const pt &l, const pt &r) {
    return l.x * r.y - l.y * r.x;
}

ptdata dot(const pt &l, const pt &r) {
    return l.x * r.x + l.y * r.y;
}


ll pwmod(ll a, ll n, ll mod) {
    ll ret = 1;
    while (n) {
        if (n & 1) ret = ret * a % mod;
        a = a * a % mod;
        n >>= 1;
    }
    return ret;
}

template<typename T>
inline T sqr(T x) {
    return x * x;
}


bool remin(ll &x, ll y) {
    if (x > y) {
        x = y;
        return 1;
    }
    return 0;
}

int n, m;

const int N = 100;
int p[N];
int ss[N];

inline int get(int v) {
    if (p[v] == v) return v;
    return p[v] = get(p[v]);
}

inline void unite(int a, int b) {
    a = get(a);
    b = get(b);
    if (a == b) return;
    if (ss[a] < ss[b]) swap(a, b);
    p[b] = a;
    ss[a] += ss[b];
}


vector<int> A;

bool check(const vector<string> &a) {
    vector<vector<int> > g(2 * n * m + n + m);
    map<PII, int> id;
    int sz = 0;
    int dx[] = {0, -1, 0, 1};
    int dy[] = {-1, 0, 1, 0};
    forn(i, n) {
        forn(j, m) {
            forn(k, 4) {
                PII p = mp(2 * i + dx[k], 2 * j + dy[k]);
                if (!id.count(p)) {
                    id[p] = sz++;
                }
            }
        }
    }
    forn(i, n) {
        forn(j, m) {
            int st = 0;
            if (a[i][j] == '\\') st = 1;
            for (int k = st; k < 4; k += 2) {
                int k1 = k;
                int k2 = (k + 1) % 4;
                PII p1 = mp(2 * i + dx[k1], 2 * j + dy[k1]);
                PII p2 = mp(2 * i + dx[k2], 2 * j + dy[k2]);
                g[id[p1]].pb(id[p2]);
                g[id[p2]].pb(id[p1]);
            }
        }
    }
    forn(i, sz) {
        p[i] = i;
        ss[i] = 1;
    }
    forn(i, sz) {
        for(int to : g[i]) {
            unite(i, to);
        }
    }
    vector<int> vv;
    int i = 0, j = 0;
    for(j = 0; j < m; ++j) {
        PII p = mp(2 * i - 1, 2 * j);
        vv.pb(id[p]);
    }
    j = m - 1;
    for(i = 0; i < n; ++i) {
        PII p = mp(2 * i, 2 * j + 1);
        vv.pb(id[p]);
    }
    i = n - 1;
    for (j = m - 1; j >= 0; --j) {
        PII p = mp(2 * i + 1, 2 * j);
        vv.pb(id[p]);
    }
    j = 0;
    for (i = n - 1; i >= 0; --i) {
        PII p = mp(2 * i, 2 * j - 1);
        vv.pb(id[p]);
    }
    for (i = 0; i < n + m; ++i) {
        if (get(vv[A[2 * i]]) != get(vv[A[2 * i + 1]])) return false;
    }
    for (i = 0; i < 2 * (n + m); i += 2) {
        for (j = i + 2; j < 2 * (n + m); j += 2) {
            if (get(vv[A[i]]) == get(vv[A[j]])) return false;
        }
    }
    return true;
}


inline void solve(int test) {
    cin >> n >> m;
    A.resize(2 * (n + m));
    forn(i, n + m) {
        cin >> A[2 * i];
        cin >> A[2 * i + 1];
        --A[2 * i];
        --A[2 * i + 1];
    }
    vector<string> b(n);
    forn(i, n) {
        b[i].assign(m, '/');
    }
    cout << "Case #" << test << ":\n";
    forn(mask, 1 << (n * m)) {
        forn(i, n) {
            forn(j, m) {
                int v = i * m + j;
                if (mask & (1 << v)) {
                    b[i][j] = '/';
                } else {
                    b[i][j] = '\\';
                }
            }
        }
        if (check(b)) {
            forn(i, n) {
                cout << b[i] << "\n";
            }
            return;
        }
    }
    cout << "IMPOSSIBLE\n";
}


int main() {
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t = 1;
    cin >> t;
    forn(i, t)
        solve(i + 1);

    cerr << "Time " << clock() / (double) CLOCKS_PER_SEC << endl;
    return 0;
}