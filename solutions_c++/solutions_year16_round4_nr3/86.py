#include <bits/stdc++.h>
using namespace std;
#define long int64_t
#define ulong uint64_t
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define cauto const auto
#define _overload3(_1,_2,_3,name,...) name
#define _rep(i,n) repi(i,0,n)
#define repi(i,a,b) for(int i=int(a);i<int(b);++i)
#define rep(...) _overload3(__VA_ARGS__,repi,_rep,)(__VA_ARGS__)
#define all(c) begin(c),end(c)
template<class C>inline void uniq(C&c){c.erase(unique(all(c)),end(c));}
template<class T>inline bool chmin(T&a,const T&b){return a>b&&(a=b,1);}
template<class T>inline bool chmax(T&a,const T&b){return a<b&&(a=b,1);}

const int N = 64;

int r, c, n, p[N];

void input()
{
    cin >> r >> c;
    n = 2 * (r + c);
    rep(i, n) cin >> p[i];
}

class disjoint_set {
    vector<int> p;
public:
    disjoint_set(int n) : p(n, -1) {}
    int root(int i) { return p[i] >= 0 ? p[i] = root(p[i]) : i; }
    int size(int i) { return -p[root(i)]; }
    bool same(int i, int j) { return root(i) == root(j); }
    bool merge(int i, int j) {
        i = root(i), j = root(j);
        if (i == j) return false;
        if (p[i] > p[j]) swap(i, j);
        p[i] += p[j], p[j] = i;
        return true;
    }
};

bool attempt(int s)
{
    const int R = 2 * r + 1;
    const int C = 2 * c + 1;
    disjoint_set uf(R * C);
    rep(i, r) rep(j, c) {
        if (s>>(i*c+j) & 1) {
            uf.merge((2*i  )*C + (2*j+1), (2*i+1)*C + (2*j  ));
            uf.merge((2*i+1)*C + (2*j+2), (2*i+2)*C + (2*j+1));
        } else {
            uf.merge((2*i  )*C + (2*j+1), (2*i+1)*C + (2*j+2));
            uf.merge((2*i+1)*C + (2*j  ), (2*i+2)*C + (2*j+1));
        }
    }
    vector<int> x(n), y(n);
    rep(i, c) {
        x[i]     = 2*i + 1;
        y[i]     = 0;
        x[i+r+c] = C - x[i] - 1;
        y[i+r+c] = R - 1;
    }
    rep(i, c, c+r) {
        x[i]     = C - 1;
        y[i]     = 2*(i-c) + 1;
        x[i+r+c] = 0;
        y[i+r+c] = R - y[i] - 1;
    }
    for (int i = 0; i < n; i += 2) {
        const int a = p[i] - 1;
        const int b = p[i+1] - 1;
        if (not uf.same(y[a]*C + x[a], y[b]*C + x[b])) {
            return false;
        }
    }
    return true;
}

void solve()
{
    rep(s, 1<<(r*c)) if (attempt(s)) {
        rep(i, r) {
            rep(j, c) cout << (s>>(i*c+j) & 1 ? '/' : '\\');
            cout << endl;
        }
        return;
    }
    cout << "IMPOSSIBLE" << endl;
}

int main()
{
    cout << fixed << setprecision(10);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        input();
        cout << "Case #" << i << ":" << endl;
        solve();
    }
}
