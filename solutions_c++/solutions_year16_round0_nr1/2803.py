#include <bits/stdc++.h>

using namespace std;

int find(int n) {
    if (n == 0) {
        return -1;
    }
    int mask = 0;
    for (int i = 1; ; ++i) {
        long long j = (long long)i * n;
        while (j > 0) {
            mask |= 1 << (j % 10);
            j /= 10;
        }
        if (mask == 1023) {
            return i;
        }
    }
}

void solve() {
    int n;
    cin >> n;
    int ans = find(n);
    if (ans == -1) {
        cout << "INSOMNIA" << endl;
    } else {
        cout << (long long)ans * n << endl;
    }
}

int main() {
//    freopen("A.in", "r", stdin);
    //freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    cin >> T;
    for (int caseId = 1; caseId <= T; ++caseId) {
        printf("Case #%d: ", caseId);
        solve();
        fflush(stdout);
    }
}
