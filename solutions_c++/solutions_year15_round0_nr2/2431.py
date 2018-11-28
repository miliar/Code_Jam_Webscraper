#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> arr(n);
    int m = 0;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        m = max(m, arr[i]);
    }

    int ans = 1e9;
    for (int i = 1; i <= m; i++) {
        int cand_ans = i;
        for (int j = 0; j < n; j++) {
            if (arr[j] > i) {
                cand_ans += (arr[j] - 1) / i;
            }
        }

        ans = min(ans, cand_ans);
    }

    printf("%d\n", ans);
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        printf("Case #%d: ", i + 1);
        solve();
    }
}
