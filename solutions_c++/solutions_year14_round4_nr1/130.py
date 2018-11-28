#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int cnt[1000];

void solve() {
    int n, X;
    scanf("%d%d", &n, &X);
    memset(cnt, 0, sizeof cnt);
    for (int i = 0; i < n; ++i) {
        int si;
        scanf("%d", &si);
        cnt[si]++;
    }
    int ans = 0;
    for (int i = 999; i >= 0; --i) {
        int j = i;
        while (cnt[i] > 0) {
            cnt[i]--;
            while (j > 0 && (j + i > X || cnt[j] == 0)) {
                j--;
            }
            if (j == 0) {
                ans++;
                //cout << i << endl;
            } else {
                ans++;
                cnt[j]--;
                //cout << i << ' ' << j << endl;
            }
        }
    }
    printf("%d\n", ans);
}

int main() {
    //freopen("A.in", "r", stdin);
    int T;
    scanf("%d", &T);
    for (int caseId = 1; caseId <= T; ++caseId) {
        printf("Case #%d: ", caseId);
        solve();
    }
}
