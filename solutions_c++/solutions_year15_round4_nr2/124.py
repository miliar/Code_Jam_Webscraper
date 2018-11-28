#include <bits/stdc++.h>//{{{
#define all(x) begin(x),end(x)
#define rall(x) (x).rbegin(),(x).rend()
#define REP(i,b,n) for(int i=(int)(b);i<(int)(n);++i)
#define rep(i,n) REP(i,0,n)
#define repsz(i,v) rep(i,(v).size())
#define aur auto&
#define bit(n) (1LL<<(n))
#define eb emplace_back
#define mt make_tuple
#define fst first
#define snd second
using namespace std;
typedef long long ll;
//#define int long long
template<class C>int size(const C &c){ return c.size(); }
template<class T>bool chmin(T&a,const T&b){if(a<=b)return false;a=b;return true;}
template<class T>bool chmax(T&a,const T&b){if(a>=b)return false;a=b;return true;}//}}}
template<typename T> T s_to(string s){ //{{{
    stringstream ss;
    T res;
    ss << s;
    ss >> res;
    return res;
} //}}}



using R = long double;
bool solve(){
    int n; cin >> n;
    R v, t; cin >> v >> t;
    vector<pair<R, R>> in;
    rep(i, n){
        R r, c; cin >> r >> c;
        in.emplace_back(c, r);
    }
    sort(all(in));
    if(n == 2 and in[0].first == in[1].first){
        in[0].second += in[1].second;
        in.pop_back();
        --n;
    }
    if(n == 2 and in[0].first == t){ in.pop_back(); --n; }
    if(n == 2 and in[1].first == t){ swap(in[0], in[1]); in.pop_back(); --n; }
    if(n == 1){
        if(in[0].first == t){
            cout << v / in[0].second << endl;
        }else{
            cout << "IMPOSSIBLE" << endl;
        }
    }else if(n == 2){
        if(in[0].first <= t and t <= in[1].first){
            R v0 = (t - in[1].first) * v;
            v0 /= in[0].first - in[1].first;
            R v1 = v - v0;
            cout << max<R>(v0 / in[0].second, v1 / in[1].second) << endl;
        }else{
            cout << "IMPOSSIBLE" << endl;
        }
    }else assert(false);
    return true;
}
signed main(){
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cout << std::fixed << std::setprecision(10);
    string s;
    getline(cin, s);
    int T = s_to<int>(s);
    rep(i, T){
        cout << "Case #" << (i+1) << ": ";
        solve();
    }
    return 0;
}
// vim:set foldmethod=marker commentstring=//%s:
