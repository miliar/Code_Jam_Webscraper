#include<bits/stdc++.h>

using namespace std;

struct _ { ios_base::Init i; _() { cin.sync_with_stdio(0); cin.tie(0); } } _;
int d;
const int mx = 1005;
int a[mx];

int main() {
    int t;
    cin >> t; 
    for(int tt = 0; tt < t; ++tt) {
        cin >> d;
        for(int i = 0; i < d; ++i) {
            cin >> a[i];
        }
        int ans = 20000009;
        for(int x = 1; x <= 1000; ++x) { 
            int ret = 0;
            for(int i = 0; i < d; ++i) {
                ret += (a[i] + x - 1) / x - 1;
            }
            ans = min(ans, ret + x);
        }
        cout << "Case #" << tt + 1 << ": " << ans << endl;
    }
    return 0;
}
