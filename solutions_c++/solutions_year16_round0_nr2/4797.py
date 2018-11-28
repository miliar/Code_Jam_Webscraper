#include <bits/stdc++.h>

using namespace std;

char s[200];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int _T;
    scanf("%d", &_T);
    for (int _t = 1; _t <= _T; _t++) {
        scanf("%s", s + 1);
        int n = strlen(s + 1);
        int flip = 0;

        for (int i = n; i >= 1; i--) {
            int x = s[i] == '+' ? 0 : 1;
            if (flip % 2 != x) {
                flip++;
            }
        }
        printf("Case #%d: %d\n", _t, flip);
    }
    return 0;
}
