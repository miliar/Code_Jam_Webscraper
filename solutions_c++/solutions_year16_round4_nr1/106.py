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

int n, r, p, s;

void input()
{
    cin >> n >> r >> p >> s;
}

const int N = 12;
string ans[N+1][3] = {"R", "P", "S"};

void gen()
{
    rep(i, N) rep(j, 3) {
        ans[i+1][j] = min(ans[i][j] + ans[i][(j+2)%3],
                          ans[i][(j+2)%3] + ans[i][j]);
    }
}

bool attempt(string cand)
{
    return (count(all(cand), 'R') == r and
            count(all(cand), 'P') == p and
            count(all(cand), 'S') == s);
}

void solve()
{
    rep(i, 3) if (attempt(ans[n][i])) {
        cout << ans[n][i] << endl;
        return;
    }
    cout << "IMPOSSIBLE" << endl;
}

int main()
{
    gen();

    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        input();
        cout << "Case #" << i << ": ";
        solve();
    }
}
