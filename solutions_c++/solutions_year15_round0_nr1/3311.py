#include <iostream>
#include <cstdio>
#include <vector>


using namespace std;


typedef long long LL;


int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    LL t;
    cin >> t;
    for (LL q = 1; q <= t; ++q) {
        string s;
        LL n;
        cin >> n >> s;
        LL ans = 0;
        LL cst = 0;
        for (LL i = 0; i <= n; ++i) {
            if (cst >= i) {
                cst += s[i] - '0'; 
            }        
            else {
                ans += i - cst;
                cst += i - cst + s[i] - '0';
            }
        }
        
        cout << "Case #" << q << ": " << ans << endl; 
    }
    return 0;
}
