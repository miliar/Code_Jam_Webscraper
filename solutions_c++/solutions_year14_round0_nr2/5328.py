#include <bits/stdc++.h>
#define sz(x) ((int)(x).size())
#define REP(i,b,n) for(int i=(int)(b);i<(int)(n);++i)
#define rep(i,n) REP(i,0,n)
#define repsz(i,v) rep(i,sz(v))
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define mt make_tuple
#define fst first
#define snd second
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define bit(x) (1LL<<x)
#define int long long
#define cauto const auto &
static const int INF = 1<<25;
static const double EPS = 1e-5;
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
template<class T> T mineq(T &a, const T &b){ return a = min(a, b); }
template<class T> T maxeq(T &a, const T &b){ return a = max(a, b); }
template<typename T> T s_to(string s){ //{{{
    stringstream ss;
    T res;
    ss << s;
    ss >> res;
    return res;
} //}}}
typedef long double R;

void solve(){
    R  c, f, x;
    cin >> c >> f >> x;
    const int up = 1000000;
    R t = 0;
    R res = 1E30;
    R spd = 2;
    rep(i, up+1){
        mineq(res, t + x / spd);
        t += c / spd;
        spd += f;
        if(res < t) break;
        assert(i < up);
    }
    cout << res << endl;
}

signed main(){
    //cin.tie(0);
    //ios_base::sync_with_stdio(0);
    cout.setf(ios::fixed); cout.precision(10);
    string s;
    getline(cin, s);
    int T = s_to<int>(s);
    rep(i, T){
        cout << "Case #" << (i+1) << ": ";
        solve();
    }
    return 0;
}
/* vim:set foldmethod=marker commentstring=//%s : */
