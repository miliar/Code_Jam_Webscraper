#include <iostream>
#include <vector>

using namespace std;

int main() {
    freopen("main.in", "r", stdin);
    freopen("main.out", "w", stdout);

    int t;
    cin >> t;
    for(int i = 0; i < t; ++i) {
        string s;
        cin >> s;
        cout << "CASE #" << i + 1 << ": ";

        vector<int> a(s.size(), 0);
        for (size_t j = 0; j < s.size(); ++j) {
            if (s[j] == '+') {
                a[j] = 1;
            }
        }

        int ans = 0;
        int last = a[0];

        for (size_t j = 0; j < a.size(); ++j) {
            if (a[j] != last) {
                ans++;
                last = a[j];
            }
        }

        if (last == 0) {
            ans++;
        }

        cout << ans << "\n";
    }

    return 0;
}