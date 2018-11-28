#include <bits/stdc++.h>

#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define in(x) int (x); input((x));
#define x first
#define y second
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)

typedef int itn;

//#define next next12345
//#define prev prev12345
#define left lefdsf232
#define right rig43783
#define x1 x12345
#define y1 y12345

using namespace std;

template<typename T>
T gcd(T x, T y) {
    while (y > 0) {
        x %= y;
        swap(x, y);
    }
    return x;
}

template<class T>
T lcm(T a, T b) {
    return a / gcd(a, b) * b;
}


template<class _T>
inline _T sqr(const _T &x) {
    return x * x;
}

template<class _T>
inline string tostr(const _T &a) {
    ostringstream os("");
    os << a;
    return os.str();
}

typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> PII;
const ld PI = 3.1415926535897932384626433832795L;

template<typename T>
inline void input(T &a) {
    static int ed;
    a = 0;
    while (!isdigit(ed = getchar()) && ed != '-') { }
    char neg = 0;
    if (ed == '-') {
        neg = 1;
        ed = getchar();
    }
    while (isdigit(ed)) {
        a = 10 * a + ed - '0';
        ed = getchar();
    }
    if (neg) a = -a;
}

template<typename T = int>
inline T nxt() {
    T res;
    input(res);
    return res;
}

void myassert(bool v) {
    assert(v);
    //cout << "FAIL\n";
    //exit(0);
}

mt19937 generator;

bool check(int v) {
    if (v < 2) return false;
    for (int i = 2; i * i <= v; ++i) {
        if (v % i == 0) {
            return false;
        }
    }
    return true;
}

long long pw(long long a, long long n, long long m) {
    ll res = 1;
    while (n) {
        if (n & 1ll) {
            res = res * a % m;
        }
        a = a * a % m;
        n >>= 1;
    }
    return res;
}

long long inv(long long a, long long p) {
    long long res = 1;
    while (a > 1) {
        res = res * (p - p / a) % p;
        a = p % a;
    }
    return res;
}

int rec(int u1, int u2, int *d, int n) {
    int res = 1;
    for (int x = 0; x < n; ++x) {
        if (u1 & (1 << x)) continue;
        int cnt = 0;
        for (int y = 0; y < n; ++y) {
            if (u2 & (1 << y)) continue;

            if (d[x] & (1 << y))
                res &= rec(u1 | (1 << x), u2 | (1 << y), d, n);

        }
        if ((u2 & d[x]) == d[x]) {
            return 0;
        }
    }
    return res;
}

int check(int n, int *d) {
    return rec(0, 0, d, n);
}

struct dsu {
    vector <int> p;
    void init(int n) {
        p.resize(n);
        iota(all(p), 0);
    }

    int get(int v) {
        if (p[v] == v) {
            return v;
        }
        return p[v] = get(p[v]);
    }

    void unite(int a, int b) {
//        cout << "ADD EDGE " << a << " " << b << endl;
        a = get(a);
        b = get(b);

        if (a == b) {
            return;
        }
        p[a] = b;
    }
};

struct T {
    string s;
    vector <int> pi;

    T() {}

    T(string x) : s(x) {
        s += "%";
        pi.resize(s.size());
        for (int i = 1; i < s.size(); ++i) {
            int j = pi[i - 1];
            while (s[i] != s[j] && j > 0) {
                j = pi[j - 1];
            }
            if (s[i] == s[j]) {
                ++j;
            }
            pi[i] = j;
        }
        state = 0;
    }

    int state;

    int add(char c) {
        while (s[state] != c && state > 0) {
            state = pi[state - 1];
        }
        if (s[state] == c) {
            ++state;
        }
    }
};

struct solution {
    int test;

    int n;
    int s;


    vector <double> x, y, z;


    void read() {
        cin >> n >> s;
        x.resize(n);
        y.resize(n);
        z.resize(n);
        for (int i = 0; i < n; ++i) {
            cin >> x[i] >> y[i] >> z[i];
            double t;
            cin >> t;
            cin >> t;
            cin >> t;
        }
    }

    double dist(int a, int b) {
        return sqrt(abs(sqr(x[a] - x[b]) + sqr(y[a] - y[b]) + sqr(z[a] - z[b])));
    }

    vector <double> d;

    void print() {
        cout << "Case #" << test << ": ";
//        cerr << solve(0, 2) << endl;
//        cerr << s << endl;
//        cout << 5ll * dp[0][s.length() / 2] << endl;
        cout << setprecision(10) << fixed;
        cout << d[1];
        cout << endl;
    }


    void solve() {
        d.assign(n, DBL_MAX);
        vector <int> u(n);
        d[0] = 0;
        forn(i, n) {
            int p = -1;
            forn(i, n) if (!u[i]) {
                    if (p == -1 || d[p] > d[i]) {
                        p = i;
                    }
                }
            u[p] = 1;
            forn (i, n) {
                d[i] = min(d[i], max(d[p], dist(i, p)));
            }
        }
    }

} * solutions;

void solve(int test) {
    solutions[test].solve();
}

int main(int argc, char ** argv) {

#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
    #define fname "sequence"
    //freopen(fname".in", "r", stdin);
    //freopen(fname".out", "w", stdout);
#endif
//    pre();
    int tests = nxt();

    solutions = new solution[tests];

    for (int i = 0; i < tests; ++i) {
        solutions[i].test = i + 1;
        solutions[i].read();
    }

    thread threads[tests];

    for (int i = 0; i < tests; ++i) {
        threads[i] = thread(solve, i);
    }

    for (int i = 0; i < tests; ++i) {
        threads[i].join();
        solutions[i].print();
    }
#ifdef LOCAL
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC * 1000 << " ms." << endl;
#endif
    return 0;
}