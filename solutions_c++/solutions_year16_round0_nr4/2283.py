#include <bits/stdc++.h>

using namespace std;

int t;

int main() {
    freopen("D.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    iostream::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> t;
    for (int r = 0; r < t; r++) {
        int k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << r + 1 << ": ";
        for (int j = 0; j < k; j++) {
            cout << j + 1 << " ";
        }
        cout << "\n";
    }
}
