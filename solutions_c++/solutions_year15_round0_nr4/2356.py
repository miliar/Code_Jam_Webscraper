#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#define min(a, b) (a) < (b) ? (a) : (b)
#define N 4

using namespace std;

bool canFill(int X, int R, int C) {

    if (R * C % X != 0) {
        return false;
    }

    if (R < X && C < X) {
        return false;
    }

    if ((R <= 1 || C <= 1) && X >= 3) {
        return false;
    }

    if (X == 4 && (R <= 2 || C <= 2)) {
        return false;
    }

    return true;
}

int main() {
    int T, X, R, C;
    scanf("%d", &T);
    for (int cnt = 1; cnt <= T; ++cnt) {
        scanf("%d %d %d", &X, &R, &C);

        if (canFill(X, R, C)) {
            printf("Case #%d: GABRIEL\n", cnt);
        } else {
            printf("Case #%d: RICHARD\n", cnt);
        }
    }

    return 0;
}