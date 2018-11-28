#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include <string.h>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    register int i, cases;
    for (cases = 0; cases < T; cases++) {
        int X, R, C;
        scanf("%d %d %d", &X, &R, &C);

        bool gabriel = true;

        if (R < X && C < X || R * 2 < X || C * 2 < X || (R * C) % X)
            gabriel = false;

        if (X == 4 && (R == 2 && R * C < 3 * X || C == 2 && R * C < 3 * X))
            gabriel = false;

        printf("Case #%d: %s\n", cases + 1, gabriel ? "GABRIEL" : "RICHARD");
    }
}
