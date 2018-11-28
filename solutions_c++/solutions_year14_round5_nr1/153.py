#include <bits/stdc++.h>
#define int ll
// def //{{{
#define REP(i,b,n) for(int i=(int)(b);i<(int)(n);++i)
#define rep(i,n) REP(i,0,n)
#define repsz(i,v) rep(i,sz(v))
#define let(v, x) typeof(x) v = (x)
#define foreach(i,v) for(let(i, (v).begin());i!=(v).end();i++)
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define mt make_tuple
#define fst first
#define snd second
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define sz(x) ((int)(x).size())
#define cauto const auto &
//}}}
using namespace std;
// typedef//{{{
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef pair<int,pii> pipii;
//}}}
// tr << ( vector, map, pair, tuple, etc... ) << endl//{{{
template <typename T, typename U>
struct sfinae_helper{typedef void type;};
template <typename T, typename U = void>
struct Print{ static ostream &pp(ostream &os, const T &x){ return os << x; } };
struct trace{//{{{
    ostream& os;
    trace(ostream& os): os(os) { }
    template<typename T>
        trace& operator<<(const T& x){ Print<T>::pp(os, x); return *this;}
    trace &operator<<(ostream& f(ostream&)){ f(os); return *this; }
    operator ostream &(){ return os; }
} tr(cout);//}}}
// Container//{{{
template <typename T> struct Print<T, typename sfinae_helper<T, typename T::iterator>::type>{
    static ostream &pp(ostream &os, const T &v){
        trace(os) << '[';
        for(const auto &x : v) trace(os) << x << ", ";
        return trace(os) << ']';
    }
};//}}}
// Pair//{{{
template <typename T> struct Print<T, typename sfinae_helper<T, typename T::first_type>::type>{
    static ostream &pp(ostream &os, const T &x){
        return trace(os) << '(' << x.first << ", " << x.second << ')';
    }
};//}}}
// Tuple//{{{
template<class T, size_t N> struct TuplePrint{
    static ostream &print(ostream &os, const T &x){
        TuplePrint<T, N-1>::print(os, x) << ", ";
        return trace(os) << get<N-1>(x);
    }
};
template<class T> struct TuplePrint<T, 1>{
    static ostream &print(ostream &os, const T &x){
        return trace(os) << get<0>(x);
    }
};
template <typename... Args>//Tuple
struct Print<tuple<Args...>>{
    static ostream &pp(ostream &os, const tuple<Args...> &x){
        os << "(";
        return TuplePrint<decltype(x), sizeof...(Args)>::print(os, x) << ")";
    }
};//}}}
//}}}
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
template<class T> T mineq(T &a, const T &b){ return a = min(a, b); }
template<class T> T maxeq(T &a, const T &b){ return a = max(a, b); }
#define bit(n) (1LL<<(n))
static const int INF = 1<<25;
static const double EPS = 1e-5;

inline void pre(){
}

inline void solve(){
    vector<ll> in;
    int n;
    {
        ll p, q, r, s;
        cin >> n >> p >> q >> r >> s;
        in.resize(n);
        rep(i, n) in[i] = (i*p+q) % r + s;
    }
    // sum [0, i)
    vector<ll> ps(n+1);
    rep(i, n) ps[i+1] = ps[i] + in[i];
    int D = 1; while(D < n) D <<= 1;

    ll res = 1LL<<50;
    rep(b, n+1){
        // [0, a), [a, b), [b, n)
        ll z = ps[n] - ps[b];
        int aa = 0;
        for(int d = D; d; d>>=1) if(aa+d < b && ps[aa+d] < z) aa += d;
        for(int a = max(0LL, aa-10); a <= min(b, aa+10); ++a){
            ll x = ps[a], y = ps[b] - ps[a];
            res = min(res, max({x, y, z}));
        }
    }
    cout << (ps[n] - res) * 1.0 / ps[n] << endl;
}

signed main(){
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

