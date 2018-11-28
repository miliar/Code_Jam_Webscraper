#include <bits/stdc++.h>
using namespace std;

int t;

char c[1005];

char neg(char c) {
    if (c == '+') {
        return '-';
    } else {
        return '+';
    }
}

int main() {
    scanf("%d", &t);
    int cs = 0;
    while (t--) {
        cs++;
        int k;
        scanf("%s %d", c, &k);
        int n = strlen(c);
        bool impossible = false;
        int res = 0;
        for (int i = 0; i < n; i++) {
            if (c[i] != '+') {
                if (i + k > n) {
                    impossible = true;
                    break;
                }
                for (int j = i;  j < i + k; j++) {
                    if (j >= n) {
                        return 0;
                    }
                    c[j] = neg(c[j]);
                }
                res = res + 1;
            }
        }
        if (impossible) {
            printf("Case #%d: IMPOSSIBLE\n", cs);
        } else {
            printf("Case #%d: %d\n", cs, res);
        }
    }
}
