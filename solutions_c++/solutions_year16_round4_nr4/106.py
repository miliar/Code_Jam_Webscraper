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


int n;

bool check(const vector<string> &a) {
    char u[n + n];
    memset(u, 0, sizeof(u));
    forn(i, n) {
        if (u[i]) continue;
        queue<int> q;
        char u2[n + n];
        memset(u2, 0, sizeof(u2));
        q.push(i);
        u2[i] = 1;
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            if (v < n) {
                forn(j, n) {
                    if (a[v][j] == '1') {
                        if (u2[j + n]) continue;
                        u2[j + n] = 1;
                        q.push(j + n);
                    }
                }
            } else {
                v -= n;
                forn(j, n) {
                    if (a[j][v] == '1') {
                        if (u2[j]) continue;
                        u2[j] = 1;
                        q.push(j);
                    }
                }
            }
        }
        int cnt[2];
        cnt[0] = cnt[1] = 0;
        forn(j, n) {
            if (u2[j]) ++cnt[0];
            if (u2[j + n]) ++cnt[1];
        }
        if (cnt[0] != cnt[1]) return false;
        forn(j, n) {
            if (!u2[j]) continue;
            forn(k, n) {
                if (!u2[k + n]) continue;
                if (a[j][k] != '1') return false;
            }
        }
        forn(j, n + n) {
            u[j] |= u2[j];
        }
    }
    return true;
}


inline void solve(int test) {
    cin >> n;
    vector<string> s(n);
    forn(i, n) {
        cin >> s[i];
    }
    int ans = n * n;
    forn(mask, 1 << (n * n)) {
        vector<string> t = s;
        forn(i, n) {
            forn(j, n) {
                int v = i * n + j;
                if (mask & (1 << v)) {
                    t[i][j] = '1';
                }
            }
        }
        if (check(t)) {
            int add = 0;
            forn(i, n) {
                forn(j, n) {
                    if (t[i][j] != s[i][j]) {
                        ++add;
                    }
                }
            }
            ans = min(ans, add);
        }
    }
    cout << "Case #" << test << ": " << ans << "\n";
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