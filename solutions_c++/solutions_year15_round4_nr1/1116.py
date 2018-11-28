#include <cstdio>

const int MAX_R = 100;
const int MAX_C = 100;

int T;
int R, C;
char M[MAX_R][MAX_C];

int answer;

bool up(int r, int c) {
    int i;
    for (i = r - 1; i >= 0; i--) {
        if (M[i][c] != '.') {
            return true;
        }
    }
    return false;
}

bool down(int r, int c) {
    int i;
    for (i = r + 1; i < R; i++) {
        if (M[i][c] != '.') {
            return true;
        }
    }
    return false;
}

bool left(int r, int c) {
    int j;
    for (j = c - 1; j >= 0; j--) {
        if (M[r][j] != '.') {
            return true;
        }
    }
    return false;
}

bool right(int r, int c) {
    int j;
    for (j = c + 1; j < C; j++) {
        if (M[r][j] != '.') {
            return true;
        }
    }
    return false;
}

int main(void) {
    int t;
    int i, j;

    // citirea datelor
    scanf("%d", &T);
    for (t = 1; t <= T; ++t) {
        scanf("%d %d", &R, &C);
        for (i = 0; i < R; ++i) {
            scanf("%s", M[i]);
        }

        // calcularea solutiei
        bool impossible = false;
        answer = 0;
        for (i = 0; i < R; ++i) {
            for (j = 0; j < C; ++j) {
                if (M[i][j] == '>' && !right(i, j)) {
                    answer++;
                }
                if (M[i][j] == '<' && !left(i, j)) {
                    answer++;
                }
                if (M[i][j] == '^' && !up(i, j)) {
                    answer++;
                }
                if (M[i][j] == 'v' && !down(i, j)) {
                    answer++;
                }
                if (M[i][j] != '.' && !(up(i, j) || down(i, j) || left(i, j) || right(i, j))) {
                    impossible = true;
                }
            }
        }

        // afisarea solutiei
        if (impossible) {
            printf("Case #%d: IMPOSSIBLE\n", t);
        } else {
            printf("Case #%d: %d\n", t, answer);
        }
    }
    return 0;
}
