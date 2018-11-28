#include <cstdio>

using namespace std;

int main() {
    freopen("D.in", "rt", stdin);
    freopen("D.out", "wt", stdout);
    int t, k, c, s;

    scanf("%d", &t);

    for (int tc = 1; tc <= t; tc++) {
        scanf("%d %d %d", &k, &c, &s);
        printf("Case #%d:", tc);
        for (int i = 1; i <= k; i++)
            printf(" %d", i);
        printf("\n");
    }

    return 0;
}
