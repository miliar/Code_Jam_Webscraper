#include <cstdio>
int kase;
int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small.out", "w", stdout);
    scanf("%d", &kase);
    for (int cas=1; cas<=kase; cas++) {
        int a, b;
        scanf("%d%d%d", &a, &b, &a);
        if (a==1) {
            printf("Case #%d: 1\n", cas);
            continue;
        }
        printf("Case #%d:", cas);
        for (int i=0; i<a; i++)
            printf(" %d", i+1);
        puts("");
    }
    return 0;
}
