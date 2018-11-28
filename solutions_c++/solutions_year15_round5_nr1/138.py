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

const int N = 5000000;

long n, d, s[N], m[N];

void input()
{
    cin >> n >> d;
    long a, c, r;
    cin >> s[0] >> a >> c >> r;
    rep(i, 1, n) {
        s[i] = (s[i-1] * a + c) % r;
    }
    cin >> m[0] >> a >> c >> r;
    rep(i, 1, n) {
        m[i] = (m[i-1] * a + c) % r;
    }
}

vector<vector<int>> T;
vector<pair<int, int>> pool;

void dfs(int v, int lo, int hi)
{
    lo = min<int>(lo, s[v]);
    hi = max<int>(hi, s[v]);
    if (hi - lo > d) return;
    pool.emplace_back(hi, lo);
    for (int c : T[v]) {
        dfs(c, lo, hi);
    }
}

void solve()
{
    T.assign(n, vector<int>());
    rep(i, 1, n) {
        T[m[i] % i].push_back(i);
    }
    pool.clear();
    dfs(0, s[0], s[0]);
    sort(all(pool));
    int ans = 1;
    priority_queue<pair<int, int>> que;
    for (auto p : pool) {
        int hi, lo;
        tie(hi, lo) = p;
        que.emplace(-lo, hi);
        while (not que.empty() and -que.top().first < hi - d) {
            que.pop();
        }
        if (hi - d <= s[0] and s[0] <= hi) {
            ans = max<int>(ans, que.size());
        }
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
