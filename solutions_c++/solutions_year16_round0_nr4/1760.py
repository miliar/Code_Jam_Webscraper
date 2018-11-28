#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int d = 1; d <= t; d++) {
        int a, b, c;
        cin >> a >> b >> c;
        cout << "Case #" << d << ": ";
        for (int p = 1; p <= a; p++) {
            cout << p << " ";
        }
        cout << endl;
    }
}
