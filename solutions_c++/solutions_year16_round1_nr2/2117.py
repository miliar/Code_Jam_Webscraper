#include <bits/stdc++.h>

using namespace std;

int main() {
    int test;
    cin >> test;
    for (int t = 1; t <= test; ++t) {
        int n;
        cin >> n;
        vector<int> freq(2500, 0);
        for (int i = 1; i <= 2 * n - 1; ++i) {
            for (int j = 1; j <= n; ++j) {
                int hold;
                cin >> hold;
                ++freq[hold];
            }
        }
        vector<int> ans;
        for (int i = 1; i <= 2500; ++i) {
            if (freq[i] & 1) {
                ans.push_back(i);
            }
        }
        cout << "Case #" << t << ": ";
        for (int e : ans) {
            cout << e << ' ';
        }
        cout << '\n';
    }
    return 0;
}
