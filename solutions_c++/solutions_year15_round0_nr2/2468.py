#include <bits/stdc++.h>
#define INF 1000000007
#define debug(x) cout << #x << " = " << (x) << endl;

using namespace std;

int main() {
    freopen("in", "r", stdin); freopen("out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        int n;
        cin >> n;
        vector<int> a;
        while (n--) {
            int b;
            cin >> b;
            a.push_back(b);
        }
        sort(a.rbegin(), a.rend());
        int k = a[0];
        int res = INF;
        for (int i = k; i > 0; i--) {
            int ops = 0, c = 0;
            for (int j = 0; j < a.size() && a[j] > i; j++) {
                    ops += a[j] / i;
                    if (a[j] % i == 0) c++;
            }
            res = min(res, ops + i - c);
        }
        cout << "Case #" << i << ": " << res << endl;
    }
    return 0;
}
