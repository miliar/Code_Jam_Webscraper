#include <bits/stdc++.h>

using namespace std;

int main() {
    int t, q = 1, count, maxn;
    string x, tmp, res;
    cin >> t;
    while(t--) {
        cin >> x;
        res = x[0];
        for (int i = 1; i < x.size(); ++i) {
            if (x[i] >= res[0]) {
                res = x[i] + res;
            } else {
                res += x[i];
            }
        }
        cout << "Case #" << q++ << ": " << res << endl;

    }
    return 0;
}
