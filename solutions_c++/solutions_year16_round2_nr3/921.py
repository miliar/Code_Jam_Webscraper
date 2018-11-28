#include <bits/stdc++.h>
using namespace std;

int n;
string c1[1005], c2[1005];
set <string> s1, s2;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int nTests = 0;
    scanf("%d", &nTests);

    for(int t = 1; t <= nTests; ++t) {
        printf("Case #%d: ", t);
        scanf("%d\n", &n);
        for(int i = 1; i <= n; ++i) {
            c1[i] = ""; c2[i] = "";
            char ch = getchar();
            do {
                c1[i] += ch;
                ch = getchar();
            } while (ch != ' ');
            ch = getchar();
            do {
                c2[i] += ch;
                ch = getchar();
            } while (ch != '\n');
        }

        int res = 0;
        for(int mask = 1; mask < (1 << n); ++mask) {
            s1.clear(); s2.clear();
            for(int i = 1; i <= n; ++i)
                if (mask & (1 << (i - 1))) {
                    s1.insert(c1[i]); s2.insert(c2[i]);
                }
            int cnt = 0;
            for(int i = 1; i <= n; ++i)
                if ((mask & (1 << (i - 1))) == 0) {
                    cnt += (s1.find(c1[i]) != s1.end() && s2.find(c2[i]) != s2.end());
                }
            res = max(res, cnt);
        }

        printf("%d\n", res);
    }

    return 0;
}
