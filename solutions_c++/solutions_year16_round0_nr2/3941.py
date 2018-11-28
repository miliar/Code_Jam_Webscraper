#include <bits/stdc++.h>
using namespace std;

const int maxn = 110;

int t;
char s[maxn];

int main() {
    scanf("%d", &t);
    for (int cas = 1; cas <= t; ++cas) {
        int ans = 0;
        scanf("%s", s);

        int n = strlen(s);
        for (int i = 0; i + 1 < n; ++i)
            if (s[i] != s[i + 1])
                ++ans;
        if (s[n - 1] == '-') ++ans;
        printf("Case #%d: %d\n", cas, ans);
    }
}
