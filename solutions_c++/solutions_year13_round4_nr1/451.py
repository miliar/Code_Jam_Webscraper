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
typedef long long ll;
typedef unsigned long long ull;
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

ll n;
ll f(ll o, ll e, ll p){
    if(o > e) swap(o, e);
    ll res = 0;
    ll d = e-o;
    res += d * n;
    res -= (d * (d-1)) / 2;
    return p * res;
}
void solve(){
    ll m;
    cin >> n >> m;
    map<ll, ll> in;
    ll res = 0;
    rep(i, m){
        ll o, e, p;
        cin >> o >> e >> p;
        if(o > e) swap(o, e);
        in[o] += p;
        in[e] -= p;
        res += f(o, e, p);
    }
//  cout<< res << endl;
    vector<pair<ll, ll> > st;
    foreach(it, in){
        if(it->snd == 0) continue;
        if(it->snd > 0){
            st.pb(mp(it->fst, it->snd));
        }else{
            ll p = -it->snd;
            while(p > 0){
                pair<ll, ll> dp = st.back(); st.pop_back();
                if(dp.snd > p){
                    st.pb(mp(dp.fst, dp.snd - p));
                    dp.snd = p;
                }
//              cout << dp.fst << "->" << it->fst << ": " << dp.snd << endl;
//              cout << f(dp.fst, it->fst, dp.snd) << endl;
                res -= f(dp.fst, it->fst, dp.snd);
                p -= dp.snd;
            }
        }
    }
    cout << res << endl;
}

int main(){
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
