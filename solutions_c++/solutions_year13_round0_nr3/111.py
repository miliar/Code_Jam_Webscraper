#include <iostream>//{{{
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <utility>
#include <algorithm>
#include <numeric>
#include <complex>
#include <functional>
#include <memory>
#include <sstream>
#include <iterator>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <cassert>
#include <ctime>
#include <cctype>//}}}
#define REP(i,b,n) for(int i=(int)(b);i<(int)(n);++i)//{{{
#define rep(i,n) REP(i,0,n)
#define repsz(i,v) rep(i,sz(v))
#define let(v, x) typeof(x) v = (x)
#define foreach(i,v) for(let(i, (v).begin());i!=(v).end();i++)
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define sz(x) ((int)(x).size()) //}}}
static const int INF = 1<<25;
static const double EPS = 1e-5;
using namespace std;//{{{
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef pair<int,pii> pipii;//}}}
template<typename T> ostream& out(T b, T e, ostream& os=cout){ //{{{
    for(; b != e; ++b != e && os << ", ")os << *b; return os;
}
template<class T> T mineq(T &a, const T &b){ return a = min(a, b); }
template<class T> T maxeq(T &a, const T &b){ return a = max(a, b); } //}}}
template<typename T> T s_to(string s){ //{{{
    stringstream ss;
    T res;
    ss << s;
    ss >> res;
    return res;
} //}}}
template<typename T> string to_s(T t){ //{{{
    stringstream ss;
    ss << t;
    return ss.str();
} //}}}
template<typename T> inline T dbl(T x){ return x*x; }

#include <gmpxx.h>
typedef mpz_class ll;

// n 桁以下の数で, 桁二乗和が s 以下の数を列挙する.
vector<ll> dfs_res;
void dfs(int n, int s, ll crr = 0){
    if(n == 0){
        dfs_res.pb(crr);
    }else{
        for(int i = 0; i * i <= s; ++i) dfs(n-1, s-i*i, crr*10+i);
    }
}

// fair integer かチェックする
bool check(ll n){
    ll s = 0;
    ll _n = n;
    ll t = 0;
    while(_n != 0){
        t *= 10;
        t += _n % 10;
        s += (_n % 10) * (_n % 10);
        _n /= 10;
    }
    if(s >= 10) return false;
    if(t != n) return false;
    return true;
}

// parindrome で桁二乗和が 10 未満の数を列挙する.
vector<ll> enum_fair(){
    dfs_res.clear();
    dfs(26, 5);
    vector<ll> candidate;
    rep(i, 10) candidate.pb(i);
    repsz(i, dfs_res){
        ll t = dfs_res[i];
        string str = to_s(t);
        string rts(rall(str));
        candidate.pb(s_to<ll>(str + rts));
        for(int mid = 0; mid < 4; ++mid)
            candidate.pb(s_to<ll>(str + string(1, '0'+mid) + rts));
    }
    vector<ll> res;
    repsz(i, candidate) if(check(candidate[i])) res.pb(candidate[i]);
    sort(all(res));
    res.erase(unique(all(res)), res.end());
    return res;
}

vector<ll> fair_integers;
void pre(){
    fair_integers = enum_fair();
//  rep(i, 50) cout << fair_integers[i] << endl;
}

// count CONST + {x < a}
int solve2(ll a){
    int res = 0;
    while(dbl(fair_integers[res]) < a) ++res;
    return res;
}

void solve(){
    ll a, b;
    cin >> a >> b;
    ++b;
    cout << solve2(b) - solve2(a) << endl;
}

int main(){
    pre();
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
