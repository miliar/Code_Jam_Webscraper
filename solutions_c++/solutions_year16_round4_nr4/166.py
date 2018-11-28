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

bool ok(const vector<string>& s, int aa) {
    int n = size(s);
    vector<int> ord(n);
    iota(all(ord), 0);

    vector<int> ord2(n);
    iota(all(ord2), 0);

    perm(ord) {
        perm(ord2) {
            // dump(ord);
            vector<int> used(n, 0);
            for (int i : ord) {
                bool done = false;
                for(int j: ord2){
                    if (!done && used[j] == 0 && s[i][j] == '1') {
                        done = true;
                        used[j] = 1;
                    }
                }
                if (!done) return false;
            }
        }
    }
    return true;
}

void submain() {
    int n;
    cin >> n;
    vector<string> s(n);
    rep(i, n) cin >> s[i];

    int U = 1 << (n * n);
    int ans = 114514;

    for (int S = 0; S < U; S++) {
        int tmp = 0;
        vector<string> t = s;
        rep(i, n) rep(j, n) {
            int k = i * n + j;

            if ((S >> k) & 1 && t[i][j] == '0') {
                tmp++;
                t[i][j] = '1';
            }
        }
        if (ans <= tmp) continue;
        if (ok(t, tmp)) chmin(ans, tmp);
    }
    cout << ans;
}

int main() {
    int TEST_CASE;
    cin >> TEST_CASE;
    for (int i = 1; i <= TEST_CASE; i++) {
        cout << "Case #" << i << ": ";
        submain();
        cout << endl;
    }
}
