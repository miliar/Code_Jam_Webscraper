#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    freopen("d.in", "r", stdin);
    freopen("d_output.txt", "w", stdout);

    int cas = 0, t, k, c, s;
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d%d", &k, &c, &s);
        if (k == 1) printf("Case #%d: 1\n", ++cas);
        else if (c == 1 && s == k) {
            printf("Case #%d:", ++cas);
            for (int i = 1; i <= k; ++i) printf(" %d", i);
            puts("");
        }
        else if (c == 1 || s + 1 < k) {
            printf("Case #%d: IMPOSSIBLE\n", ++cas);
        }
        else {
            printf("Case #%d:", ++cas);
            for (int i = 2; i <= k; ++i) printf(" %d", i);
            puts("");
        }
    }

    return 0;
}
