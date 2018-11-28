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

typedef ll ptdata;

const int K = 27;
const ll inf = 1ll << (K - 1);
const ll mask = 1ll << K;

struct pt {
    ptdata x, y;

    pt() { }

    pt(ptdata x, ptdata y) : x(x), y(y) { }

    inline pt operator-(const pt &r) const {
        return pt(x - r.x, y - r.y);
    }

    inline pt operator+(const pt &r) const {
        return pt(x + r.x, y + r.y);
    }

    inline pt operator*(const ld &r) const {
        return pt(x * r, y * r);
    }

    inline ptdata sqlen() const {
        return abs(x * x + y * y);
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
    inline ll hash() const {
        return ((x + inf) << K) | (y + inf);
    }
};

ostream &operator << (ostream &os, const pt &p) {
    return os << "(" << p.x << "," << p.y << ")";
}

inline pt ptFromHash(ll hash) {
    ll y = (hash - inf) & (mask - 1);
    ll x = (hash >> K) - inf;
    return pt(x, y);
}

inline ptdata cross(const pt &l, const pt &r) {
    return l.x * r.y - l.y * r.x;
}

inline ptdata dot(const pt &l, const pt &r) {
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

string prepare(const string &s) {
    string t(2 * s.length() + 3, 'a');
    t[0] = '^';
    t[1] = '#';
    for (int i = 0; i < (int)s.length(); ++i) {
        t[2 * i + 2] = s[i];
        t[2 * i + 3] = '#';
    }
    t[2 * s.length() + 2] = '&';
    return t;
}

vector<int> manacher(const string &s) {
    assert(!s.empty());
    string t = prepare(s);
    vector<int> p(t.length(), 0);
    int c = 0, r = 0;
    for (int i = 1; i + 1 < (int)t.length(); ++i) {
        int j = 2 * c - i;
        p[i] = (r > i) ? min(r - i, p[j]) : 0;
        while (t[i - p[i] - 1] == t[i + p[i] + 1]) {
            ++p[i];
        }
        if (i + p[i] > r) {
            c = i;
            r = i + p[i];
        }
    }
    vector<int> ret(2 * s.length() - 1);
    for (int i = 0; i < int(2 * s.length() - 1); ++i) {
        ret[i] = p[i + 2];
    }
    return ret;
}

inline void solve(int test) {
    string s;
    cin >> s;

    int ans = 0;
    while (!s.empty()) {
        assert(s.length() % 2 == 0);
        vector<int> t = manacher(s);
        vector<int> even;
        for (int i = 1; i < t.size(); i += 2) {
            even.push_back(t[i]);
        }
        if (*max_element(all(even)) == 0) break;
        vector<int> pos;
        for (int i = 0, r = 0; i < even.size(); ++i) {
            if (i - even[i] / 2 + 1 < r) continue;
            if (even[i] > 0) {
                pos.push_back(i);
                r = i + even[i] / 2 + 1;
            }
        }
        int sum = 0;
        for (int x : pos) {
            sum += even[x] / 2;
            assert(even[x] % 2 == 0);
        }
        ans += sum * 10;
        char used[s.length()];
        memset(used, 0, sizeof(used));
        for (int x : pos) {
            int l = x - even[x] / 2 + 1;
            int r = x + even[x] / 2;
            for (int j = l; j <= r; ++j) {
                assert(!used[j]);
                used[j] = 1;
            }
        }
        string tm;
        for (int i = 0; i < s.length(); ++i) {
            if (used[i]) continue;
            tm.push_back(s[i]);
        }
        s.swap(tm);
    }
    ans += (s.length() / 2) * 5;
    cout << "Case #" << test << ": " << ans << "\n";
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
    forn(i, t)
        solve(i + 1);

    //cerr << "Time " << clock() / (double) CLOCKS_PER_SEC << endl;
    return 0;
}