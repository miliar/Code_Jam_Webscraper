#include <bits/stdc++.h>
using namespace std;
#define ulong uint64_t
#define mt make_tuple
#define eb emplace_back
#define all(u) begin(u),end(u)
#define _overload3(_1,_2,_3,name,...) name
#define _rep(i,n) _repi(i,0,n)
#define _repi(i,a,b) for(int i=int(a);i<int(b);++i)
#define rep(...) _overload3(__VA_ARGS__,_repi,_rep,)(__VA_ARGS__)
template<class C>void uniq(C&c){c.erase(unique(all(c)),end(c));}
template<class T>bool chmin(T&a,const T&b){return a>b&&(a=b,1);}
template<class T>bool chmax(T&a,const T&b){return a<b&&(a=b,1);}

const int N = 128;

int n, m;
char table[N][N];

void input()
{
    cin >> n >> m;
    rep(i, n) cin >> table[i];
}

const string s = "v>^<";
const int di[] = {1, 0,-1, 0};
const int dj[] = {0, 1, 0,-1};
inline bool in(int i, int j) { return 0 <= i and i < n and 0 <= j and j < m; }

void solve()
{
    int ans = 0;
    rep(i, n) rep(j, m) if (table[i][j] != '.') {
        int flag = 0, away = 0;
        rep(dir, 4) {
            int ti = i, tj = j;
            do {
                ti += di[dir], tj += dj[dir];
            } while (in(ti, tj) and table[ti][tj] == '.');
            if (in(ti, tj)) {
                flag = 1;
            } else if (table[i][j] == s[dir]) {
                away = 1;
            }
        }
        if (away and !flag) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
        ans += away;
    }
    cout << ans << endl;
}

int main()
{
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(10);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        input();
        cout << "Case #" << i << ": ";
        solve();
    }
}
