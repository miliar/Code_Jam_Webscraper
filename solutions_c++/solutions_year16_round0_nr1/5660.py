#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <numeric>
#include <limits>
using namespace std;

int main() {
    freopen("A-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        int n; cin >> n;
        vector<bool> b(10);
        int ans, s = 0;
        for (ans = 1; ans < 100; ans++) {
            int k = n * ans;
            while(k > 0) {
                int d = k % 10;
                if (!b[d]) {
                    b[d] = true;
                    s ++;
                }
                k /= 10;
            }
            if (s == 10) break;
        }
        cout << "Case #" << t << ": ";
        if (ans < 100) cout << ans * n;
        else cout << "INSOMNIA";
        cout << endl;
    }
    return 0;
}
