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
bool check(vector<int> &c){
    bool ret = true;
    rep(i, 10){
        if (c[i] == 0) {
            ret = false;
        }
    }
    return ret;
}


int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);
//    freopen("testout.txt", "w", stdout);
    // source code
    
    int T;
    cin >> T;
    rep(i, T){
        int N;
        cin >> N;
        cout << "Case #" << i + 1 << ": ";
        if (N == 0) {
            output("INSOMNIA", 0);
        }
        else{
            vector<int> c(10, 0);
            ll now = 0;
            while(1){
                now += N;
                ll tmp = now;
                while (tmp > 0) {
                    c[tmp % 10] = 1;
                    tmp /= 10;
                }
                if (check(c)) {
                    break;
                }
            }
            cout << now << endl;
        }
    }
    
    
    
    return 0;
}