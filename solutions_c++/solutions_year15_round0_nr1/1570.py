#include <bits/stdc++.h>
using namespace std;

int main() {
    int T, smax;
    char s[1010];

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %s", &smax, s);
        int ans = 0, cnt = 0;
        for (int i = 0; i <= smax; i++) {
            if (cnt < i) {
                ans += i-cnt;
                cnt = i;
            }
            cnt += s[i]-'0';
        }
        printf("Case #%d: %d\n", t, ans);
    }
}
