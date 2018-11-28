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

bool check(string &s){
    bool ret = true;
    rep(i, s.size()){
        if (s[i] ==  '-') {
            ret = false;
        }
    }
    return ret;
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    // source code
    int N;
    cin >> N;
    rep(i, N) {
        string s;
        cin >> s;
        cout << "Case #" << i + 1 << ": ";
         int ans = 0;
        while (!check(s)) {
            char top = s[0];
            int ind = 0;
            while (ind < s.size() - 1) {
                if (top != s[ind + 1]) {
                    break;
                }
                ind++;
            }
            reverse(s.begin(), s.begin() + ind);
            rep(i, ind + 1){
                if (s[i] == '-') {
                    s[i] = '+';
                }
                else{
                    s[i] = '-';
                }
            }
//            cout << ans << ": " << s << endl;
            ans++;
        }
        cout << ans << endl;
    }
    
    return 0;
}