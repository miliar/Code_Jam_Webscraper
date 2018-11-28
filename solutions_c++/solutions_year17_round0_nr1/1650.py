#include <bits/stdc++.h>

using namespace std;

void flip(char s[], int i, int k)
{
    while (k--) {
        if (s[i] == '+') {
            s[i] = '-';
        } else {
            s[i] = '+';
        }
        i++;
    }
}

int main()
{
    int t;
    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &t);
    for (int x = 1; x <= t; x++) {
        char s[1001];
        int k;
        scanf("%s%d", s, &k);
        int l = strlen(s);
        int ans = 0;
        for (int i = 0; i <= l - k; i++) {
            if (s[i] != '-') {
                continue;
            }
            ans++;
            flip(s, i, k);
        }
        for (int i = 0; i < l; i++) {
            if (s[i] == '-') {
                ans = -1;
                break;
            }
        }
        if (ans < 0) {
            printf("Case #%d: IMPOSSIBLE\n", x);
        } else {
            printf("Case #%d: %d\n", x, ans);
        }
    }
    return 0;
}
