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
unordered_map<int, R> memo[30];
int n;
int ps[30], ss[30];
int y;
R res;
void dfs(int S, int i, R pos, R mn){//{{{
    if(S == (1<<n)-1){chmin(res, mn); return;}
    if(i >= 0 and memo[i].count(S) and memo[i][S] <= mn) return;
    if(i >= 0) memo[i][S] = mn;

    vector<pair<R, int>> left, right;
    rep(j, n) if(!(S>>j&1)){
        if(ps[j] < 0){ left.emplace_back( abs((ps[j] - mn * ss[j]) - pos) / (y - ss[j]), j); }
        else         {right.emplace_back( abs((ps[j] + mn * ss[j]) - pos) / (y - ss[j]), j); }
    }
    sort(all(left));
    sort(all(right));
    int mask = S;
    for(auto &l : left){
        mask |= 1 << l.second;
        dfs(mask, l.second, pos - l.first * y, mn + l.first);
    }
    mask = S;
    for(auto &r : right){
        mask |= 1 << r.second;
        dfs(mask, r.second, pos + r.first * y, mn + r.first);
    }
}//}}}

bool solve(){
    res = 1. / 0.;
    rep(i, n) memo[i].clear();
    cin >> y >> n;
    rep(i, n) cin >> ps[i];
    rep(i, n) cin >> ss[i];
    dfs(0, -1, (R)0, (R)0);
    cout << res << endl;
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
