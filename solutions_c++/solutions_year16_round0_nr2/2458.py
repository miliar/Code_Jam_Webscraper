#include <bits/stdc++.h>
char s[110];

int main() {
    //freopen("D://B-large.in", "r", stdin);
    //freopen("D://B-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int ca = 1; ca <= t; ++ca) {
        scanf("%s", s);
        int len = strlen(s);
        s[len] = '+';
        int ans = 0;
        for(int i = 0; i < len; ++i) if(s[i] != s[i+1]) ++ans;
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}
