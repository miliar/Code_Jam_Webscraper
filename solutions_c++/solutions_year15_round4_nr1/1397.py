#define _CRT_SECURE_NO_WARNINGS
//#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
//#define int ll
//#define endl "\n"
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
#define all(c) (c).begin(), (c).end()
#define loop(i,a,b) for(ll i=a; i<ll(b); i++)
#define rep(i,b) loop(i,0,b)
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define mt make_tuple
template<class T> ostream & operator<<(ostream & os, vector<T> const &);
template<int n, class...T> typename enable_if<(n>=sizeof...(T))>::type _ot(ostream &, tuple<T...> const &){}
template<int n, class...T> typename enable_if<(n< sizeof...(T))>::type _ot(ostream & os, tuple<T...> const & t){ os << (n==0?"":" ") << get<n>(t); _ot<n+1>(os, t); }
template<class...T> ostream & operator<<(ostream & os, tuple<T...> const & t){ _ot<0>(os, t); return os; }
template<class T, class U> ostream & operator<<(ostream & os, pair<T,U> const & p){ return os << "(" << p.first << ", " << p.second << ") "; }
template<class T> ostream & operator<<(ostream & os, vector<T> const & v){ rep(i,v.size()) os << v[i] << (i+1==(int)v.size()?"":" "); return os; }
template<class T> inline bool chmax(T & x, T const & y){ return x<y ? x=y,true : false; }
template<class T> inline bool chmin(T & x, T const & y){ return x>y ? x=y,true : false; }
#ifdef DEBUG
#define dump(...) (cerr<<#__VA_ARGS__<<" = "<<mt(__VA_ARGS__)<<" ["<<__LINE__<<"]"<<endl)
#else
#define dump(...)
#endif
// ll const mod = 1000000007;
// ll const inf = 1LL<<60;

int solve(int const R, int const C, vector<string> const g){
    int di[256],dj[256];
    di[(int)'^'] = -1;
    di[(int)'v'] = +1;
    di[(int)'>'] = 0;
    di[(int)'<'] = 0;

    dj[(int)'^'] = 0;
    dj[(int)'v'] = 0;
    dj[(int)'>'] = +1;
    dj[(int)'<'] = -1;
    auto inside = [&](int i, int j){
        return 0 <= i && i < R && 0 <= j && j < C;
    };

    int ans = 0;
    rep(i,R){
        rep(j,C){
            if(g[i][j] == '.') continue;
            char dir = g[i][j];
            int ci, cj;
            ci = i+di[(int)dir], cj = j+dj[(int)dir];

            while(inside(ci,cj) && g[ci][cj]=='.'){
                ci += di[(int)dir], cj += dj[(int)dir];
            }
            if(inside(ci,cj)) continue;
            bool ok = false;
            for(char ndir : {'>','<','^','v'}){
                if(ndir == dir) continue;
                ci = i+di[(int)ndir], cj = j+dj[(int)ndir];
                while(inside(ci,cj) && g[ci][cj]=='.'){
                    ci += di[(int)ndir], cj += dj[(int)ndir];
                }
                if(inside(ci,cj)) ok = true;
            }
            //dump(i,j,ci,cj,ok);
            if(ok) ans++;
            else return -1;
        }
    }
    return ans;
}

signed main(){
    int t;
    cin >> t;
    rep(i,t){
        int R,C;
        cin >> R >> C;
        vector<string> g(R);
        rep(i,R) cin >> g[i];
        int ans = solve(R,C,g);
        if(ans != -1) printf("Case #%d: %d\n", signed(i+1), signed(ans));
        else printf("Case #%d: %s\n", signed(i+1), "IMPOSSIBLE");
    }
}
