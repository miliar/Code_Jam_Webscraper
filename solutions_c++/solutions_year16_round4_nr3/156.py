#define DINGER_GISBAR
#include <bits/stdc++.h>
using namespace std;
const long long MOD = static_cast<int>(1e9) + 7;
//{{{TEMPLATE_BEGIN
#include <unistd.h>
using namespace std::rel_ops;
#ifdef ZEROKUGI
#include <dumper.hpp>
#define dump(x) dumper::dumper(cerr, __LINE__, (#x), (x), 50, 1, 1)
#define tick(...) dumper::tick(__VA_ARGS__)
#pragma message "Compiling " __FILE__
#else
#define dump(x)
#define tick(...)
#endif
typedef long long lint;
typedef unsigned long long ulint;
typedef long double ldouble;
typedef vector<int> vint;
#define rep(i, n) \
    for (int i = 0, i##_len = static_cast<int>(n); i < i##_len; i++)
#define all(c) begin(c), end(c)
#define perm(c)   \
    sort(all(c)); \
    for (bool c##p = 1; c##p; c##p = next_permutation(all(c)))
#define uniquenize(v) (v).erase(unique(all(v)), end(v))
#define size(c) (int)((c).size())
#define cauto const auto &
#define memset(x, y) memset(x, y, sizeof(x))
#define popcount __builtin_popcount
#define gcd __gcd
inline lint bit(int x) { return 1LL << x; }
template <class T>
inline bool chmin(T& a, const T& b) {
    return a > b ? a = b, 1 : 0;
}
template <class T>
inline bool chmax(T& a, const T& b) {
    return a < b ? a = b, 1 : 0;
}
template <class T>
inline pair<vector<T>, char> operator*(const vector<T>& v, const char& c) {
    return make_pair(v, c);
}
template <class T>
inline istream& operator>>(istream& is, vector<T>& v) {
#ifdef ZEROKUGI
    if (v.empty()) {
        cerr << "Error L" << __LINE__ << ": vector size is zero." << endl;
        exit(EXIT_FAILURE);
    }
#endif
    for (auto& x : v) is >> x;
    return is;
}
template <class T>
inline ostream& operator<<(ostream& os, const pair<vector<T>, char>& v) {
    bool t = 0;
    for (const T& x : v.first) {
        if (t) os << v.second;
        os << x;
        t = 1;
    }
    return os;
}
template <class T>
inline ostream& operator<<(ostream& os, vector<T>& v) {
    return os << v * ' ';
}
struct before_main {
    before_main() {
        cin.tie(0);
        ios::sync_with_stdio(0);
        cout << fixed << setprecision(20);
        tick(0, 0);
    };
} __before_main;
//}}}TEMPLATE_END

struct pos {
    int y, x, d;
};

char s[100][100];
int r, c;

pos to_pos(int x) {
    if (x <= c) return {0, x - 1, 0};
    if (x <= c + r) return {x - 1 - c, c - 1, 1};
    if (x <= c + r + c) return {r - 1, c - (x - r - c), 2};
    return {r - (x - c - r - c), 0, 3};
}

int to_num(pos p) {
    if (p.y == 0 && p.d == 0) {
        return p.x + 1;
    }
    if (p.x == c - 1 && p.d == 1) {
        return c + p.y + 1;
    }
    if (p.y == r - 1 && p.d == 2) {
        return c + r + (c - p.x);
    }
    if (p.x == 0 && p.d == 3) {
        return c + r + c + (r - p.y);
    }
    return -1;
}

int go(int v) {
    pos p = to_pos(v);

    while (true) {
        if (s[p.y][p.x] == '/') {
            p.d = 3 - p.d;
        } else if (s[p.y][p.x] == '\\') {
            p.d ^= 1;
        } else {
        }

        if (to_num(p) != -1) {
            return to_num(p);
        }
        if (p.d == 0) {
            p.d = 2;
            p.y--;
        } else if (p.d == 1) {
            p.d = 3;
            p.x++;
        } else if (p.d == 2) {
            p.d = 0;
            p.y++;
        } else if (p.d == 3) {
            p.d = 1;
            p.x--;
        }
    }
}

bool ok(const vector<int>& v) {
    for (int i = 0; i < size(v); i += 2) {
        if (go(v[i]) != v[i + 1]) return false;
    }
    return true;
}

void submain() {
    cin >> r >> c;

    int n = 2 * r + 2 * c;
    vector<int> v(n);
    rep(i, n) cin >> v[i];

    int U = 1<<(r*c);
    rep(S, U) {
        rep(i, r) rep(j, c) {
            int k = i * c + j;
            if ((S >> k) & 1) {
                s[i][j] = '/';
            } else {
                s[i][j] = '\\';
            }
        }
        if (ok(v)) {
            rep(i, r) {
                rep(j, c) cout << s[i][j];
                cout << endl;
            }
            return;
        }
    }
    cout << "IMPOSSIBLE" << endl;
}

int main() {
    int TEST_CASE;
    cin >> TEST_CASE;
    for (int i = 1; i <= TEST_CASE; i++) {
        cout << "Case #" << i << ":" << endl;
        submain();
    }
}
