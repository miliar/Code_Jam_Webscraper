#include <bits/stdc++.h>
#define sz(x) ((int)(x).size())
#define REP(i,b,n) for(int i=(int)(b);i<(int)(n);++i)
#define rep(i,n) REP(i,0,n)
#define repsz(i,v) rep(i,sz(v))
//#define let(v, x) typeof(x) v = (x)
//#define foreach(i,v) for(let(i, (v).begin());i!=(v).end();i++)
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

constexpr auto n = 4;
void solve(){
    vector<vector<int>> a(n, vector<int>(n));
    int res = bit(30)-1;

    rep(_, 2){
        int r; cin >> r; --r;
        rep(i, n) rep(j, n) cin >> a[i][j];
        int tmp = 0;
        rep(j, n) tmp |= bit(a[r][j]);
        res &= tmp;
    }
    if(res == 0){
        cout << "Volunteer cheated!" << endl;
    }else if(res == (res & -res)){
        rep(i, 30) if(res>>i&1) cout << i << endl;
    }else{
        cout << "Bad magician!" << endl;
    }
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
