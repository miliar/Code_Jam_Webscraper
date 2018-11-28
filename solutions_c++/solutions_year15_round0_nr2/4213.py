#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

int p[1001], T;

void solve() {
    int n;
    int maxp;
    scanf("%d", &n);
    for (int i=0; i<n; i++) {
        scanf("%d", &p[i]);
        maxp = max(p[i], maxp);
    }
    int l = 1, r = maxp;
    while (l < r) {
        int m = (l + r) / 2;
        bool can = false;
        for (int i=0; i<m; i++) {
            int cur = 0;
            for (int j=0; j<n; j++) {
                cur += (p[j] - 1) / (m - i);
                if (cur > i) break;
            }
            if (cur <= i) {
                can = true;
                break;
            }
        }
        if (can) {
            r = m;
        } else {
            l = m + 1;
        }
    }
    printf("%d", l);
}

int main() {
    freopen("b.txt", "r", stdin);
    scanf("%d", &T);
    for (int i=1; i<=T; i++) {
        printf("Case #%d: ", i);
        solve();
        printf("\n");
    }
    return 0;
}
