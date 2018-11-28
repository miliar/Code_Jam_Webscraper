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
    map<char, int> dx, dy;
    dx['>'] = dx['<'] = 0;
    dx['^'] = -1; dx['v'] = 1;
    dy['>'] = 1; dy['<'] = -1;
    dy['^'] = 0; dy['v'] = 0;

    int h, w;
    cin >> h >> w;
    vector<string> in(h);
    rep(i, h) cin >> in[i];
    int res = 0;
    rep(i, h) rep(j, w) if(in[i][j] != '.'){
        {
            int ii = i, jj = j;
            bool ok = false;
            while(true){
                ii += dx[in[i][j]]; jj += dy[in[i][j]];
                if(ii < 0 or ii >= h or jj < 0 or jj >= w) break;
                if(in[ii][jj] == '.') continue;
                ok = true;
                break;
            }
            if(ok) continue;
        }
        {
            bool ok = false;
            REP(dx, -1, 2) REP(dy, -1, 2) if(abs(dx) + abs(dy) == 1){
                int ii = i, jj = j;
                while(true){
                    ii += dx; jj += dy;
                    if(ii < 0 or ii >= h or jj < 0 or jj >= w) break;
                    if(in[ii][jj] == '.') continue;
                    ok = true;
                    break;
                }
                if(ok) break;
            }
            if(!ok){
                cout << "IMPOSSIBLE" << endl;
                return true;
            }
            ++res;
        }
    }
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
