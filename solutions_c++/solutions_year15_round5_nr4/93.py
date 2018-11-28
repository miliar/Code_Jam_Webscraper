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

bool solve(){
    int n; cin >> n;
    vector<int> es(n);
    vector<int> fs(n);
    rep(i, n) cin >> es[i];
    rep(i, n) cin >> fs[i];
    vector<int> res;
    vector<int> sums;
    unordered_map<int, int> id;
    rep(i, n) id[es[i]] = i;
    --fs[0];
    sums.emplace_back(0);
    rep(i, n) if(fs[i]){
        int t = size(sums);
        res.eb(es[i]);
        rep(A, t){
            sums.eb(sums[A] + es[i]);
            --fs[id[sums[A] + es[i]]];
        }
        --i; continue;
    }
    repsz(i, res){
        if(i) cout << " ";
        cout << res[i];
    }
        cout << endl;
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
