#include <bits/stdc++.h>

using namespace std;

int main() {
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; ++t) {
        char inp[101], s[101];
        scanf("%s", inp);
        int len = strlen(inp);
        int n = 0;
        for (int i = 0; i < len; ) {
            if (inp[i] == '+') {
                s[n++] = '+';
                while (inp[i] == '+' && i < len) ++i;
            }
            else {
                s[n++] = '-';
                while (inp[i] == '-' && i < len) ++i;
            }
        }
        int plus[n], minus[n];
        plus[0] = (s[0] == '+') ? 0 : 1;
        minus[0] = (s[0] == '-') ? 0 : 1;
        for (int i = 1; i < n; ++i) {
            plus[i] = (s[i] == '+') ? plus[i - 1] : minus[i - 1] + 1;
            minus[i] = (s[i] == '-') ? minus[i - 1] : plus[i - 1] + 1;
        }
        printf("Case #%d: %d\n", t, plus[n - 1]);
    }
    return 0;
}
