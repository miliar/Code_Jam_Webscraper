#include <bits/stdc++.h>

using namespace std;

int jizz() {
    int n; scanf("%d", &n);

    char str[1011];
    scanf("%s", str);

    int ans = 0;
    int acc = 0;

    for (int i = 0; i <= n; ++i) {
        if (acc < i) {
            ans += i - acc;
            acc = i;
        }

        int c = str[i] - '0';
        acc += c;
    }

    return ans;
}

int main() {
    int T; scanf("%d", &T); for (int t = 1; t <= T; ++t)
        printf("Case #%d: %d\n", t, jizz());
    return 0;
}