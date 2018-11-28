#include <bits/stdc++.h>

using namespace std;

void solve() {
    string s;
    cin >> s;
    int n = s.size();
    int ans = 0;
    for (int i = 0; i < n; ++i) if (s[i] == '-') {
        int j = i + 1;
        while (j < n && s[j] == '-') {
            j++;
        }
        if (i == 0) {
            ans += 1;
        } else {
            ans += 2;
        }
        i = j - 1;
    }
    cout << ans << endl;
}

int main() {
//    freopen("B.in", "r", stdin);
    //freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    
    int T;
    cin >> T;
    for (int caseId = 1; caseId <= T; ++caseId) {
        printf("Case #%d: ", caseId);
        solve();
        fflush(stdout);
    }
}
