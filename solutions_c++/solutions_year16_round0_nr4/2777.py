#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int nmax = 150005;
const long double PI = acos(-1.0);
const ll mod = 1e9 + 7;
const long double eps = 1e-6;
int main(){
    //ios_base::sync_with_stdio(0);
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for(int q = 1; q <= t; ++q){
        int k, c, s;
        cin >> k >> c >> s;
        if (c == 1){
            if (s < k) cout << "Case #" << q << ": IMPOSSIBLE\n";
            else {
                cout << "Case #" << q << ": ";
                for(int i = 1; i <= k; ++i) cout << i << ' ';
                cout << '\n';
            }
            continue;
        }
        else {
            if (s < k - 1) cout << "Case #" << q << ": IMPOSSIBLE\n";
            else {
                cout << "Case #" << q << ": ";
                for(int i = 0; i < s; ++i) cout << k * (i + 1) << ' ';
                cout << '\n';
            }
        }
    }
    return 0;
}
