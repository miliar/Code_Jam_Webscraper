#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

#define MAXN 10

int main() {
    int ncas, cnt = 0;
    
    freopen("D-small-attempt0.in", "r", stdin);
    //freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);

    scanf("%d", &ncas);
    while (ncas--) {
        int x, r, c;
        scanf("%d%d%d", &x, &r, &c);
        printf("Case #%d: ", ++cnt);
        if (x == 1) {
            printf("GABRIEL\n");
            continue;
        } else if (x == 2) {
            if (r * c % 2 == 0)
                printf("GABRIEL\n");
            else
                printf("RICHARD\n");
        } else if (x == 3) {
            if (r == 3 && c == 3)
                printf("GABRIEL\n");
            else if (r == 3 && c % 2 == 0)
                printf("GABRIEL\n");
            else if (c == 3 && r % 2 == 0)
                printf("GABRIEL\n");
            else
                printf("RICHARD\n");
        } else {
            if (r == 4 && c == 4)
                printf("GABRIEL\n");
            else if (r == 3 && c == 4)
                printf("GABRIEL\n");
            else if (r == 4 && c == 3)
                printf("GABRIEL\n");
            else
                printf("RICHARD\n");
        }
    }
    return 0;
}
