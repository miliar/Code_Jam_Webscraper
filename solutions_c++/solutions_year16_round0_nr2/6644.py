#include<bits/stdc++.h>

using namespace std;

int n, t;

char s[109];

int main() {
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);

    scanf("%d", &t);

    for (int h=1; h<=t; h++) {
        scanf("%s", &s);

        n = strlen(s);

        int ans = 1;

        for (int i=1; i<n; i++)
            if (s[i] != s[i-1])
                ans++;

        if (s[n-1] == '+') ans--;

        printf("Case #%d: %d\n", h, ans);
    }

    return 0;
}
