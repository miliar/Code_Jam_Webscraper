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

int n, m;
vector<string> A;

void input()
{
    cin >> n;
    A.resize(n);
    rep(i, n) cin >> A[i];
    m = 0;
    rep(i, n) m += count(all(A[i]), '1');
}

void solve()
{
    vector<pair<int,int> > coms;
    vector<int> ved(2*n);
    rep(s, 2*n) if (not ved[s]) {
        int wo = 0, ma = 0;
        queue<int> q;
        q.push(s);
        ved[s] = 1;
        while (not q.empty()) {
            const int v = q.front();
            q.pop();
            if (v < n) {
                ++wo;
                rep(i, n) if (A[v][i] == '1' and not ved[n + i]) {
                    q.push(n + i);
                    ved[n + i] = true;
                }
            } else {
                ++ma;
                rep(i, n) if (A[i][v - n] == '1' and not ved[i]) {
                    q.push(i);
                    ved[i] = true;
                }
            }
        }
        cerr<<"("<<wo<<","<<ma<<") ";
        coms.emplace_back(wo, ma);
    }
    cerr<<endl;
    const int inf = 10000;
    static int dp[1<<8];
    fill_n(dp, 1<<8, inf);
    dp[0] = 0;
    const int V = coms.size();
    rep(s, 1<<V) for (int t = s; t; t = (t-1)&s) {
        int wo = 0, ma = 0;
        rep(i, V) if (t >> i & 1) {
            wo += coms[i].first;
            ma += coms[i].second;
        }
        if (wo == ma) {
            chmin(dp[s], dp[s^t] + wo * ma);
        }
        if (t == (1<<V)-1 and wo != ma) {
            assert(false);
        }
    }
    cout << dp[(1<<V)-1] - m << endl;
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
