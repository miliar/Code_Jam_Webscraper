#include <bits/stdc++.h>

using namespace std;

int t;

int main() {
    freopen("A.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    iostream::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> t;
    for (int r = 0; r < t; r++) {
        int i;
        cin >> i;
        cout << "Case #" << r + 1 << ": ";
        if (i == 0) {
            cout << "INSOMNIA\n";
            continue;
        }
        long long ii = i;
        set<int> s;
        long long iii = ii;
        while (iii != 0) {
            s.insert(iii % 10);
            iii /= 10;
        }
        int cnt = 0;
        while (s.size() != 10) {
            cnt++;
            ii += i;
            iii = ii;
            while (iii != 0) {
                s.insert(iii % 10);
                iii /= 10;
            }
        }
        cout << ii << "\n";
    }
}
