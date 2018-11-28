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

const int N = 10010;

long n, a[N], b[N];
vector<pair<long, long>> vec;

void input()
{
    cin >> n;
    rep(i, n) cin >> a[i];
    rep(i, n) cin >> b[i];
    vec.clear();
    rep(i, n) vec.eb(a[i], b[i]);
    sort(all(vec));
}

void solve()
{
    vector<long> ans;
    int z = __builtin_ctz(vec[0].second);
    rep(i, z) ans.pb(0);
    rep(i, n) vec[i].second >>= z;
    rep(i, 1, n) {
        long a, b;
        tie(a, b) = vec[i];
        rep(_, b) ans.pb(a);
        rep(_, b) {
            queue<pair<long, long>> del;
            rep(j, n) {
                while (not del.empty() and del.front().first <= vec[j].first) {
                    if (del.front().first == vec[j].first) {
                        vec[j].second -= del.front().second;
                    }
                    del.pop();
                }
                del.emplace(vec[j].first + a, vec[j].second);
            }
        }
    }
    rep(i, ans.size()) cout << (i ? " " : "") << ans[i];
    cout << endl;
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
