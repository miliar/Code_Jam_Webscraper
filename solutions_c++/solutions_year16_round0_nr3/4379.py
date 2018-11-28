#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <numeric>
#include <functional>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <sstream>
#include <string>
#define repd(i,a,b) for (int i=(int)(a);i<(int)(b);i++)
#define rep(i,n) repd(i,0,n)
#define all(x) (x).begin(),(x).end()
#define mod 1000000007
#define inf 2000000007
#define mp make_pair
#define pb push_back
typedef long long ll;
using namespace std;
template <typename T>
inline void output(T a, int p) {
    if(p) cout << fixed << setprecision(p)  << a << "\n";
    else cout << a << "\n";
}
// end of template


ll pow_(ll a, ll b){
    ll ret = 1;
    rep(i, b) ret *= a;
    return ret;
}

bool check(vector<ll> &v){
    bool ret = true;
    rep(i, v.size()){
        if (v[i] == -1) {
            ret = false;
        }
    }
    return ret;
}
template <typename T> inline void voutput(T &v){
    rep(i, v.size()){
        if (i) cout << " " << v[i];
        else cout << v[i];
    }
    cout << endl;
}

string conv_bit(int n, int N){
    string s = "";
    for (int i = N - 1; i >= 0; i--) {
        if (n >> i & 1) {
            s += '1';
        }
        else{
            s += '0';
        }
    }
    return s;
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    // source code
    
    int N = 16, J = 50;
    int ans = 0;
    cout << "Case #1:" << endl;
    rep(i, 1 << (N - 2)){
        vector<ll> div(9, -1);
        repd(j, 2, 11){
            ll num = 1 + pow_((ll)j, (ll)N - 1);
            repd(k, 0, N - 2){
                if (i >> k & 1) {
                    num += pow_((ll)j, (ll)k + 1);
                }
            }
//            cout << j << ": " << num << endl;
            for (ll k = 2; k * k <= num; k++) {
                if (num % k == 0) {
                    div[j - 2] = k;
                    break;
                }
            }
        }
        
        if (check(div)) {
            cout << "1" << conv_bit(i, N - 2) << "1 ";
            voutput(div);
            ans++;
        }
        if (ans >= J) {
            break;
        }
        
    }
    
    return 0;
}