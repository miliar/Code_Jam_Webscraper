#include<stdio.h>

int main()
{
    //freopen("D-small-attempt1.in", "r", stdin);
    //freopen("out_D1.txt", "w", stdout);

    int T, X, R, C, x, aux;
    scanf("%d", &T);
    for (x = 1; x <= T; x++) {
        scanf("%d %d %d", &X, &R, &C);
        printf("Case #%d: ", x);
        if (X == 1) {
            printf("GABRIEL"); // who builds
        }
        else if (X == 2) {
            if ((R*C)%2 == 0)
                printf("GABRIEL");
            else
                printf("RICHARD");
        }
        else if (X == 3) {
            if ((R*C)%3 == 0 && R > 1 && C > 1)
                printf("GABRIEL");
            else
                printf("RICHARD");
        }
        else {
            if (R > C) {
                aux = R; R = C; C = aux;
            }
            if ((R*C)%4 == 0 && (R == 3 || R == 4))
                printf("GABRIEL");
            else
                printf("RICHARD");
        }
        printf("\n");
    }
    return 0;
}
