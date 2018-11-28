#include <iostream>
using namespace std;
int main () {
    freopen ("C:\\A-large.in", "r", stdin);
    freopen ("C:\\out.txt", "w", stdout);
    ios :: sync_with_stdio (false);
    cin.tie (0);
    int t;
    cin >> t;
    for (int casen = 1; casen <= t; ++casen){
        int ans = 0;
        int s;
        int sum = 0;
        cin >> s;
        for (int i = 0; i <= s; ++i) {
            char c;
            cin >> c;
            int n = c - '0';
            if (sum < i && n) {
               ans += i - sum;
               sum = i;
            }
            sum += n;
        } 
        cout << "Case #" << casen << ": " << ans << endl;
    }
    return 0;
}
