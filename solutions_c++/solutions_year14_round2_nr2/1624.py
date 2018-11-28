#include <bits/stdc++.h>
#define msg(x) cout << #x << " = " << x << endl
using namespace std;

int a, b, k;
int t;

int main() {
    freopen("b-small.txt", "w", stdout);
    cin.sync_with_stdio(0); cin.tie(0);
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        cin >> a >> b >> k;
        int ans = 0;
        for (int i = 0; i < a; i++) {
            for (int j = 0; j < b; j++) {
                if ((i & j) < k) ++ans;
            }
        }
        cout << "Case #" << tc << ": " << ans << "\n";
    }
    return 0;
}
