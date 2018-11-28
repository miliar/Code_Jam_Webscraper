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

bool check(string s) {
    while (s.length() > 1) {
        string x;
        for (int i = 0; i < s.length(); i += 2) {
            if (s[i] == s[i + 1]) return false;
            if (s[i] == 'R') {
                if (s[i + 1] == 'S') {
                    x += 'R';
                } else {
                    x += 'P';
                }
            }
            if (s[i] == 'S') {
                if (s[i + 1] == 'P') {
                    x += 'S';
                } else {
                    x += 'R';
                }
            }
            if (s[i] == 'P') {
                if (s[i + 1] == 'R') {
                    x += 'P';
                } else {
                    x += 'S';
                }
            }
        }
        s = x;
    }
    return true;
}

vector <string> a[13];

string get(int x, char c) {
    if (x == 0) {
        return string(1, c);
    }
    vector <char> z;
    if (c == 'S') {
        z.pb('P');
        z.pb('S');
    }
    if (c == 'R') {
        z.pb('R');
        z.pb('S');
    }
    if (c == 'P') {
        z.pb('P');
        z.pb('R');
    }
    string a = get(x - 1, z[0]);
    string b = get(x - 1, z[1]);
    return min(a + b, b + a);
}

void pre() {

    for (int i = 0; i <= 12; ++i) {
        a[i].pb(get(i, 'P'));
        a[i].pb(get(i, 'R'));
        a[i].pb(get(i, 'S'));
    }
}

struct solution {
    int test;
    string ans;

    void read() {
        int n = nxt();
        int r = nxt();
        int p = nxt();
        int s = nxt();

        for (const auto q : a[n]) {
            int c1 = count(all(q), 'R');
            int c2 = count(all(q), 'P');
            int c3 = count(all(q), 'S');
            if (c1 == r && c2 == p && c3 == s) {
                if (ans != "") {
                    ans = min(ans, q);
                } else {
                    ans = q;
                }
                return;
            }
        }
        ans = "IMPOSSIBLE";
    }

    void print() {
        cout << "Case #" << test << ": ";
        cout << ans << "\n";

    }

    void solve() {
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
    pre();
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