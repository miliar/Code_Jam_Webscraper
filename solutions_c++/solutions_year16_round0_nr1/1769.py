#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    long long t, n, cnt = 0;
    cin >> t;
    while (t--) {
        cin >> n;
        cnt++;
        cout << "Case #" << cnt << ": ";
        if (n == 0) {
            cout << "INSOMNIA" << endl;
        } else {
            long long last = 0;
            set <int> digits;
            int i = 1;
            while (digits.size() < 10) {
                long long p = i * n;
                while (p > 0) {
                    digits.insert(p % 10);
                    p /= 10;
                }
                last = i * n;
                i++;
            }
            cout << last << endl;
        }
    }
}
