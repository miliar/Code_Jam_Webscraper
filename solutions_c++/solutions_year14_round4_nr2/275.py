#include <stdio.h>
#include <algorithm>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int n, a[2048];

int solve() {
    int ans = 0;
    rep (k, n) {
        int c1 = 0, c2 = 0;
        rep (i, n) if (a[i] > a[k]) {
            if (i < k) c1++; else c2++;
        }
        ans += min(c1, c2);
    }
    return ans;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int _q = 0; _q < T; _q++) {
        scanf("%d", &n);
        rep (i, n) scanf("%d", a+i);
        printf("Case #%d: %d\n", _q+1, solve());
    }
    return 0;
}
