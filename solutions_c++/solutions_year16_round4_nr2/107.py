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

const int N = 216;

int n, k;
double p[N];

void input()
{
    cin >> n >> k;
    rep(i, n) cin >> p[i];
}

double attempt(const vector<double>& vec)
{
    static double dp[N][N];
    rep(i, N) fill_n(dp[i], N, 0.0);
    dp[0][0] = 1.0;

    assert((int)vec.size() == k);
    rep(i, k) rep(j, i+1) {
        dp[i+1][j]   += dp[i][j] * (1.0 - vec[i]);
        dp[i+1][j+1] += dp[i][j] * vec[i];
    }
    return dp[k][k/2];
}

void solve()
{
    double ans = 0.0;
    sort(p, p + n);
    rep(i, k+1) {
        vector<double> v(p, p + i);
        v.insert(end(v), p + n - (k-i), p + n);
        chmax(ans, attempt(v));
    }
    cout << ans << endl;
}

int main()
{
    cout << fixed << setprecision(10);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        input();
        cout << "Case #" << i << ": ";
        solve();
    }
}
