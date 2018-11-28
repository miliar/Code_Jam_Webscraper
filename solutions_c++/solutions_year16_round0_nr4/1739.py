#include <bits/stdc++.h>
using namespace std;

int main(void) {
    if (fopen("d-small.in", "r")) {
        freopen("d-small.in", "r", stdin);
        freopen("d-small.out", "w", stdout);
    }
    int t, k, c, s;
    cin >> t;
    for (int ii = 1; ii <= t; ii++) {
        cin >> k >> c >> s;
        printf("Case #%d:", ii);
        for (int i = 1; i <= k; i++) printf(" %d", i);
        printf("\n");
    }
    return 0;
}
