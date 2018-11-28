#include <stdio.h>
#include <cmath>

int main() {
    int T, X, R, C;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        scanf("%d%d%d", &X, &R, &C);
        int size = R * C;
        if (X == 1) 
            printf("Case #%d: GABRIEL\n", t + 1);
        else if ((X == 2) && (size % 2 == 0) )
            printf("Case #%d: GABRIEL\n", t + 1);
        else if ((X == 3) && (fmin(R,C) >= 2)  && (size % 3 == 0))
            printf("Case #%d: GABRIEL\n", t + 1);
        else if ((X == 4) && ((size == 12) || (size == 16) ) )
            printf("Case #%d: GABRIEL\n", t + 1);
        else printf("Case #%d: RICHARD\n", t + 1);
    }
}
