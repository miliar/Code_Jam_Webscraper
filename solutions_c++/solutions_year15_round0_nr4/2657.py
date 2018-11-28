#include <cstdio>

int T;
int X, R, C;

int main () {
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &T);
    
    for (int x = 1; x <= T; x++) {
        scanf("%d %d %d", &X, &R, &C);
        if (X == 1) {
            printf("Case #%d: GABRIEL\n", x);
        } else if (X == 2) {
            if ((R * C) % 2 == 0) {
                printf("Case #%d: GABRIEL\n", x);
            } else {
                printf("Case #%d: RICHARD\n", x);
            }
        } else if (X == 3) {
            if (R == 1 || C == 1) {
                printf("Case #%d: RICHARD\n", x);
            } else if ((R * C) % 3 == 0) {
                printf("Case #%d: GABRIEL\n", x);
            } else {
                printf("Case #%d: RICHARD\n", x);
            }
        } else {
            if (R == 1 || C == 1 || R == 2 || C == 2) {
                printf("Case #%d: RICHARD\n", x);
            } else if ((R * C) % 4 == 0) {
                printf("Case #%d: GABRIEL\n", x);
            } else {
                printf("Case #%d: RICHARD\n", x);
            }
        }
    }
    
    return 0;
}