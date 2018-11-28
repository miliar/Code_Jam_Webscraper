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

struct Data {
    string s;
    int S, R, P;
    bool operator < (const Data &r) const {
        if (S != r.S) return S < r.S;
        if (R != r.R) return R < r.R;
        if (P != r.P) return P < r.P;
        return false;
    }
    bool operator == (const Data &r) const {
        if (S != r.S) return false;
        if (R != r.R) return false;
        if (P != r.P) return false;
        return true;
    }
};

map<char, set<Data> > m[13];

void prepare() {
    m[0]['S'].insert(Data{"S", 1, 0, 0});
    m[0]['R'].insert(Data{"R", 0, 1, 0});
    m[0]['P'].insert(Data{"P", 0, 0, 1});

    string w = "SPR";
    for (int i = 1; i < 13; ++i) {
        for (int j = 0; j < 3; ++j) {
            int nj = (j + 1) % 3;
            for (Data d : m[i - 1][w[j]]) {
                for (Data d2 : m[i - 1][w[nj]]) {
                    string ss = (d.s < d2.s) ? d.s + d2.s : d2.s + d.s;
                    int S = d.S + d2.S;
                    int R = d.R + d2.R;
                    int P = d.P + d2.P;
                    m[i][w[j]].insert(Data{ss, S, R, P});
                }
            }
        }
    }
}

inline void solve(int test) {
    int n, R, P, S;
    cin >> n >> R >> P >> S;
    Data d = Data{"", S, R, P};
    cout << "Case #" << test << ": ";
    string res = "";
    string w = "SRP";
    for (int i = 0; i < 3; ++i) {
        if (m[n][w[i]].find(d) != m[n][w[i]].end()) {
            string cur = m[n][w[i]].find(d)->s;
            if (res.empty() || res > cur) res = cur;
        }
    }
    if (res.empty()) {
        cout << "IMPOSSIBLE\n";
    } else {
        cout << res << "\n";
    }
}


int main() {
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
    cin.tie(0);


    prepare();

    int t = 1;
    cin >> t;
    forn(i, t)
        solve(i + 1);

    cerr << "Time " << clock() / (double) CLOCKS_PER_SEC << endl;
    return 0;
}