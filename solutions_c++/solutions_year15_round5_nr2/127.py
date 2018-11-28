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

const int N = 2015;

long n, k, a[N];

void input()
{
    cin >> n >> k;
    rep(i, n-k+1) cin >> a[i];
    if (a[0] < 0) rep(i, n-k+1) a[i] = -a[i];
}

void solve()
{
    vector<pair<long, long>> vec;
    long mx = 0;
    rep(i, k) {
        long t, lo, hi;
        t = lo = hi = 0;
        for (int j = i; j < n-k; j += k) {
            t += a[j+1] - a[j];
            lo = min(lo, t);
            hi = max(hi, t);
        }
        vec.eb(lo, hi);
        mx = max(mx, hi - lo);
    }
    long rem = 0, fre = 0;
    for (auto p : vec) {
        long lo, hi;
        tie(lo, hi) = p;
        rem = (rem + k - lo % k) % k;
        fre += mx - (hi - lo);
    }
    long target = a[0] % k;
    long diff = ((target - rem) % k + k) % k;
    if (diff <= fre) {
        cout << mx << endl;
    } else {
        cout << mx + 1 << endl;
    }
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
