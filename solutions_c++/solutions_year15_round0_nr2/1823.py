#include <iostream>
#include <algorithm>
using namespace std;
int main () {
    ios :: sync_with_stdio (false);
    cin.tie (0);
    freopen ("C:\\B-large.in", "r", stdin);
    freopen ("C:\\out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int c = 1; c <= t; ++c) {
        int p;
        cin >> p;
        int n [1001] = {0};
        while (p --> 0) {
            int i;
            cin >> i;
            ++n [i];
        } 
        int ans = (int) 1e9;
        for (int i = 1; i <= 1000; ++i) {
            int d = 0;
            for (int j = i + 1; j <= 1000; ++j) 
                d += (j - 1) / i * n [j];
            d += i;
            ans = min (ans, d);
        }
        cout << "Case #" << c << ": " << ans << endl;
    }
    return 0;
}
