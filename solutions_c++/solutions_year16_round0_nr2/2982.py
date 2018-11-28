#include <cstring>
#include <cstdio>
#include <bitset>

using namespace std;

char s[105];
bitset<105> b;

int main() {
    freopen("B.in", "rt", stdin);
    freopen("B.out", "wt", stdout);
    int t;

    scanf("%d ", &t);

    for (int tc = 1; tc <= t; tc++) {
        gets(s);
        int n = strlen(s);

        b.reset();
        for (int i = 0; i < n; i++)
            if (s[i] == '+') b[i] = true;

        int ans = 0;
        while (b.count() < n) {
            int i, j = 0;
            for (i = 0; i < n; i++)
                if (!b[i]) {
                    j = i;
                    while (j < n && !b[j]) j++;
                    break;
                }
            for (i = 0; i < j; i++)
                b[i] = !b[i];
            ans++;
        }

        printf("Case #%d: %d\n", tc, ans);
    }

    return 0;
}
