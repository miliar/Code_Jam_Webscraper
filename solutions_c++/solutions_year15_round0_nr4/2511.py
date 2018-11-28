#include <cstdio>
#include <vector>

const char* YES = "GABRIEL";
const char* NO = "RICHARD";

bool solve(int X, int R, int C) {
    if (X == 1) {
        return true;
    } else if (X == 2) {
        return R % 2 == 0 ? true : C % 2 == 0;
    } else if (X == 3) {
        if (R * C % 3 != 0 || R == 1 || C == 1) {
            return false;
        } else {
            return true;
        }
    } else {
        if (R <= 2 || C <= 2 || R*C % 4 != 0) {
            return false;
        } else {
            return true;
        }
    }
}

int main(){
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        int X, R, C;
        scanf("%d", &X);
        scanf("%d", &R);
        scanf("%d", &C);

        bool gabrielCanWin = solve(X, R, C);

        const char* answer;
        if (gabrielCanWin) {
            answer = YES;
        } else {
            answer = NO;
        }
        // Print answer
        printf("Case #%d: %s\n", i, answer);
    }
    return 0;
}
