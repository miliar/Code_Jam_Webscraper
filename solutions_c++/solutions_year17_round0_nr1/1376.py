#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
#ifdef D
    // freopen("A.in", "r", stdin);
#endif
    int T; scanf("%d", &T);
    for (int kase = 1; kase <= T; kase++) {
        string s; int k; cin >> s >> k;
        int ans = 0;
        int len = s.size();
        for (int i = 0; i <= len-k; i++) {
            if (s[i] != '+') {
                for (int j = i; j < i+k; j++) {
                    s[j] = s[j] == '-' ? '+' : '-';
                }
                ans++;
            }
        }

        for (auto ch : s) {
            if (ch == '-') ans = -1;
        }

        printf("Case #%d: ", kase);
        if (ans >= 0) printf("%d\n", ans);
        else puts("IMPOSSIBLE");
    }

    return 0;
}