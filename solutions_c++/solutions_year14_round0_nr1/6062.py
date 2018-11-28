#include <cstdio>

int cs, a[17], b[17];

inline void work() {
    int p, q, ans = 0;
    scanf("%d", &p);
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j) {
            int x;
            scanf("%d", &x);
            a[x] = i + 1;
        }
    scanf("%d", &q);
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j) {
            int x;
            scanf("%d", &x);
            b[x] = i + 1;
        }
    printf("Case #%d: ", ++cs);
    for (int i = 1; i < 17; ++i)
        if (a[i] == p && b[i] == q)
            if (ans) {
                puts("Bad magician!");
                return;
            }
            else
                ans = i;
    if (ans)
        printf("%d\n", ans);
    else
        puts("Volunteer cheated!");
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--)
        work();
    return 0;
}
