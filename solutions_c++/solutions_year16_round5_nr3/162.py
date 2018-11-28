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
#define cauto const auto &
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

int x[2525], y[2525], z[2525];

struct UnionFind{
    vector<int> par;
    UnionFind(int size):par(size){
        iota(begin(par),end(par),0);
    }

    int root(int a){
        if(a == par[a]) return a;
        return par[a] = root(par[a]);
    }

    void unite(int A, int B){
        par[root(B)] = root(A);
    }

    bool eq(int a, int b){
        return root(a) == root(b);
    }
};

struct e{
    int v, w;
    int z;
};

void submain() {
    int n, s;
    cin >> n >> s;
    for (int i = 0; i < n; i++) {
        cin >> x[i] >> y[i] >> z[i];
        int aa;
        cin >> aa >> aa >> aa;
    }

    vector<e> E;

    rep(i, n) rep(j, i) {
        int d = 0;
        d += (x[i] - x[j]) * (x[i] - x[j]);
        d += (y[i] - y[j]) * (y[i] - y[j]);
        d += (z[i] - z[j]) * (z[i] - z[j]);
        E.push_back({i, j, d});
    }

    sort(all(E), [](e p, e q){
            return p.z < q.z;
            });


    UnionFind uf(n);
    for(cauto ee: E){
        uf.unite(ee.v, ee.w);
        if(uf.eq(0, 1)){
            cout << sqrt(ee.z);
            return;
        }
    }
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
