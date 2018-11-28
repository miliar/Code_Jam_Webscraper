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

const int N = 200;
double p[N];
double ip[N];
int n, k;

double solve1() {
    int mans = 0;
    double ans = 0;
    int k2 = k / 2;
    for (int mask = 0; mask < (1 << n); ++mask) {
        if (__builtin_popcount(mask) != k) continue;
        vector<int> id;
        forn(i, n) {
            if (mask & (1 << i)) {
                id.pb(i);
            }
        }
        double dp[k + 1][k2 + 2];
        memset(dp, 0, sizeof(dp));
        dp[0][0] = 1;
        forn(i, k) {
            forn(j, k2 + 1) {
                dp[i + 1][j] += dp[i][j] * ip[id[i]];
                dp[i + 1][j + 1] += dp[i][j] * p[id[i]];
            }
        }
        if (remax(ans, dp[k][k2])) {
            mans = mask;
        }
    }
    forn(i, n) {
        if (mans & (1 << i)) {
            cout << "1";
        } else {
            cout << "0";
        }
    }
    cout << endl;
    return ans;
}


double solve2() {
    double ans = 0;
    int k2 = k / 2;
    forn(i, k + 1) {
        vector<int> id;
        forn(j, i) {
            id.pb(j);
        }
        int t = k - i;
        forn(j, t) {
            id.pb(n - 1 - j);
        }
        double dp[k + 1][k2 + 2];
        memset(dp, 0, sizeof(dp));
        dp[0][0] = 1;
        forn(i, k) {
            forn(j, k2 + 1) {
                dp[i + 1][j] += dp[i][j] * ip[id[i]];
                dp[i + 1][j + 1] += dp[i][j] * p[id[i]];
            }
        }
        remax(ans, dp[k][k2]);
    }
    return ans;
}


inline void solve(int test) {
    cin >> n >> k;
    forn(i, n) {
        cin >> p[i];
    }
    sort(p, p + n);
    forn(i, n) {
        ip[i] = 1.0 - p[i];
    }

    //double ans1 = solve1();
    double ans2 = solve2();
    //cout << ans1 << " " << ans2 << endl;
    //assert(fabs(ans1 - ans2) < 1e-8);

    cout << "Case #" << test << ": ";
    cout << setprecision(10) << fixed;
    cout << ans2 << "\n";
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