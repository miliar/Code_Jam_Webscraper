#include <bits/stdc++.h>

#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define for1(i, n) for(int i = 1; i <= (int)(n); i++)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
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
    ptdata x, y, z;

    pt() { }

    pt(ptdata x, ptdata y, ptdata z) : x(x), y(y), z(z) { }

    inline pt operator-(const pt &r) const {
        return pt(x - r.x, y - r.y, z - r.z);
    }

    inline pt operator+(const pt &r) const {
        return pt(x + r.x, y + r.y, z + r.z);
    }

    inline pt operator*(const ld &r) const {
        return pt(x * r, y * r, z * r);
    }

    inline ptdata sqlen() const {
        return abs(x * x + y * y + z * z);
    }

    ld len() const {
        return sqrtl(sqlen());
    }

    inline bool operator<(const pt &r) const {
        if (x != r.x) return x < r.x;
        return y < r.y;
    }

    inline bool operator==(const pt &r) const {
        return x == r.x && y == r.y;
    }
};

ostream &operator << (ostream &os, const pt &p) {
    return os << "(" << p.x << "," << p.y << ")";
}

inline pt cross(const pt &l, const pt &r) {
    return pt(l.y * r.z - l.z * r.y,
              l.z * r.x - l.x * r.z,
              l.x * r.y - l.y * r.x);
}

inline ptdata dot(const pt &l, const pt &r) {
    return l.x * r.x + l.y * r.y + l.z * r.z;
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

struct Asteroid {
    pt s, v;
};

const ld inf = 1e7;

inline ld getDistance(const Asteroid &a, const Asteroid &b, ld t) {
    pt aa1 = a.s + a.v * t;
    pt bb1 = b.s + b.v * t;
    return (aa1 - bb1).len();
}

inline ld findMinimalDistance(const Asteroid &a, const Asteroid &b) {
    ld l = 0, r = inf;
    int it = 55;
    while (it--) {
        ld m1 = (2 * l + r) / 3;
        ld m2 = (l + 2 * r) / 3;
        ld d1 = getDistance(a, b, m1);
        ld d2 = getDistance(a, b, m2);
        if (d1 < d2) {
            r = m2;
        } else {
            l = m1;
        }
    }
    return (l + r) / 2.0;
}


const ld eps = 1e-10;


inline pair<ld, ld> timeInterval(const Asteroid &a, const Asteroid &b, ld dist) {
    ld C = (a.s - b.s).sqlen();
    ld A = (a.v - b.v).sqlen();
    ld B = dot(a.s - b.s, a.v - b.v) * 2;
    C -= dist * dist;
    if (fabs(A) < eps) {
        if (getDistance(a, b, 0) < dist) {
            return pair<ld, ld>(0, inf);
        } else {
            return pair<ld, ld>(-1, -1);
        }
    }
    ld D = B * B - 4 * A * C;
    if (D <= 0) return pair<ld, ld>(-1, -1);
    D = sqrtl(D);
    ld t1 = (-B - D) / 2 / A;
    ld t2 = (-B + D) / 2 / A;
    if (t1 > t2) swap(t1, t2);
    t1 = max(t1, 0.0L);
    if (t1 >= t2) return pair<ld, ld>(-1, -1);
    return pair<ld, ld>(t1, t2);
}

int n;
int s;
const int N = 1000;
Asteroid a[N];

pair<ld, ld> t[N][N];

inline pair<ld, ld> intersect(const pair<ld, ld> &a, const pair<ld, ld> &b) {
    pair<ld, ld> ret;
    ret.first = max(a.first, b.first);
    ret.second = min(a.second, b.second);
    return ret;
}

inline bool bool_intersect(const pair<ld, ld> &a, const pair<ld, ld> &b) {
    pair<ld, ld> ret;
    ret.first = max(a.first, b.first);
    ret.second = min(a.second, b.second);
    return ret.first <= ret.second;
}

int q[N * N];
char used[N * N];

vector<pair<pair<ld, ld>, int>> G[N];

inline bool check(ld dist) {
    forn(i, n) {
        for (int j = i + 1; j < n; ++j) {
            t[i][j] = t[j][i] = timeInterval(a[i], a[j], dist);
        }
        t[i][i] = pair<ld, ld>(0, inf);
    }
//    cerr << dist << endl;
//    forn(i, n) {
//        forn(j, n) {
//            cerr << "(" << t[i][j].first << "," << t[i][j].second << ")";
//        }
//        cerr << endl;
//    }
//    cerr << endl;
    forn(i, n) {
        G[i].clear();
    }
    forn(i, n) {
        forn(j, n) {
            if (i == j) continue;
            if (t[i][j].second < 0) {
                continue;
            }
            G[i].push_back(mp(t[i][j], j));
        }
        sort(all(G[i]), [&](const pair<pair<ld, ld>, int> &l, const pair<pair<ld, ld>, int> &r){
            return l.first.first < r.first.first;
        });
    }
    int ptr[N];
    memset(ptr, 0, sizeof(ptr));
    int q1 = 0, q2 = 0;
    memset(used, 0, sizeof(used));
    ld R = s;
    while (ptr[0] < G[0].size() && G[0][ptr[0]].first.first < R) {
        R = max(R, G[0][ptr[0]].first.second);
        int v = G[0][ptr[0]].second;
        used[v] = 1;
        q[q2++] = v;
        ++ptr[0];
    }
    while (q1 < q2) {
        int pa = q[q1++];
        int v = pa / n;
        int u = pa % n;
        if (v == 1 || u == 1) return true;
        R = t[v][u].second + s;
        while (ptr[v] < G[v].size() && G[v][ptr[v]].first.first < R) {
            R = max(R, G[v][ptr[v]].first.second);
            if (bool_intersect(pair<ld, ld>(t[v][u].first, t[v][u].second + s), G[v][ptr[v]].first)) {
                int i = G[v][ptr[v]].second;
                int pato;
                if (i < v) {
                    pato = i * n + v;
                } else {
                    pato = v * n + i;
                }
                if (!used[pato]) {
                    used[pato] = 1;
                    q[q2++] = pato;
                }
            }
            ++ptr[v];
        }
        swap(u, v);
        R = t[v][u].second + s;
        while (ptr[v] < G[v].size() && G[v][ptr[v]].first.first < R) {
            R = max(R, G[v][ptr[v]].first.second);
            if (bool_intersect(pair<ld, ld>(t[v][u].first, t[v][u].second + s), G[v][ptr[v]].first)) {
                int i = G[v][ptr[v]].second;
                int pato;
                if (i < v) {
                    pato = i * n + v;
                } else {
                    pato = v * n + i;
                }
                if (!used[pato]) {
                    used[pato] = 1;
                    q[q2++] = pato;
                }
            }
            ++ptr[v];
        }
    }
    return false;
}

inline void solve(int test) {
    cin >> n;
    cin >> s;
    cerr << test << " " << n << endl;
    forn(i, n) {
        cin >> a[i].s.x >> a[i].s.y >> a[i].s.z;
        cin >> a[i].v.x >> a[i].v.y >> a[i].v.z;
    }
    ld l = 0, r = 3000;
    int it = 40;
    while (it--) {
        ld m = (l + r) / 2.0;
        if (check(m)) {
            r = m;
        } else {
            l = m;
        }
    }
    ld ans = (l + r) / 2.0;
    cout << setprecision(10) << fixed;
    cout << "Case #" << test << ": " << ans << endl;
}


int main() {
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t = 100;
    cin >> t;
    forn(i, t) {
        solve(i + 1);
    }

    //cerr << "Time " << clock() / (double) CLOCKS_PER_SEC << endl;
    return 0;
}