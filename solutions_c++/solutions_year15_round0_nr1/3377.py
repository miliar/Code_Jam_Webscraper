#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    ios_base::sync_with_stdio(0);
    int tests;
    cin >> tests;
    for (int t = 1; t <= tests; t++) {
        int n;
        int ans = 0;
        string in;
        cin >> n;
        cin >> in;
        int pref = 0;
        for (int i = 0; i < in.size(); i++) {
            ans = max(ans, i - pref);
            pref += (in[i] - '0');
        }
        cout << "Case #" << t << ": " << ans << "\n";
    }
    return 0;
}
