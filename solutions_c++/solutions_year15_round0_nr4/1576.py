#include <cstdio>
#include <cassert>

const int GABRIEL = 1;
const int RICHARD = 2;

int T;
int X, R, C;

int answer;

int main(void) {
    int t;

    // citirea datelor
    scanf("%d", &T);
    for (t = 1; t <= T; ++t) {
        scanf("%d %d %d", &X, &R, &C);

        // calcularea solutiei
        if (R > C) {
            R ^= C;
            C ^= R;
            R ^= C;
        }
        assert(R <= C);
        if ((R * C) % X != 0) {
            answer = RICHARD;
        } else if (C < X) { // && R < X
            answer = RICHARD;
        } else if (X == 4 && R == 1) { // && C == 4
            answer = RICHARD;
        } else if (X == 4 && R == 2) { // && C == 4
            answer = RICHARD;
        } else if (X == 3 && C == 3 && R == 1) {
            answer = RICHARD;
        } else {
            answer = GABRIEL;
        }

        // afisarea solutiei
        if (answer == GABRIEL) {
            printf("Case #%d: GABRIEL\n", t);
        } else { // if (answer == RICHARD)
            printf("Case #%d: RICHARD\n", t);
        }
    }
    return 0;
}
