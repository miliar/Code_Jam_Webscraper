#include <cstdio>
#include <cstring>

#define SIZE 4
#define CLEAR(x) (memset(x, 0, sizeof(x)))

const char *X_WON = "X won";
const char *O_WON = "O won";
const char *DRAW = "Draw";
const char *NOT_COMPLETE = "Game has not completed";

int O_row[SIZE];
int O_col[SIZE];
int O_cross[2];

int X_row[SIZE];
int X_col[SIZE];
int X_cross[2];

int dot_count;

inline void clear_input() {
    dot_count = 0;
    CLEAR(O_row);
    CLEAR(O_col);
    CLEAR(O_cross);
    CLEAR(X_row);
    CLEAR(X_col);
    CLEAR(X_cross);
}

inline void read_input() {
    char in;

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            scanf("%c", &in);

            switch (in) {
                case 'X':
                    X_row[i] += 1;
                    X_col[j] += 1;
                    if (i == j) {
                        X_cross[0] += 1;
                    } else if (i + j == SIZE - 1) {
                        X_cross[1] += 1;
                    }
                    break;
                case 'O':
                    O_row[i] += 1;
                    O_col[j] += 1;
                    if (i == j) {
                        O_cross[0] += 1;
                    } else if (i + j == SIZE - 1) {
                        O_cross[1] += 1;
                    }
                    break;
                case 'T':
                    X_row[i] += 1;
                    X_col[j] += 1;
                    O_row[i] += 1;
                    O_col[j] += 1;
                    if (i == j) {
                        X_cross[0] += 1;
                        O_cross[0] += 1;
                    } else if (i + j == SIZE - 1) {
                        X_cross[1] += 1;
                        O_cross[1] += 1;
                    }
                    break;
                case '.':
                    dot_count++;
                    break;
            }
        }
        scanf("\n");
    }
    scanf("\n");
}

/*
inline void print_input() {
    printf("\n");
    printf("X_row: %d %d %d %d\n", X_row[0], X_row[1], X_row[2], X_row[3]);
    printf("X_col: %d %d %d %d\n", X_col[0], X_col[1], X_col[2], X_col[3]);
    printf("X_cross: %d %d\n", X_cross[0], X_cross[1]);
    printf("\n");
    printf("O_row: %d %d %d %d\n", O_row[0], O_row[1], O_row[2], O_row[3]);
    printf("O_col: %d %d %d %d\n", O_col[0], O_col[1], O_col[2], O_col[3]);
    printf("O_cross: %d %d\n", O_cross[0], O_cross[1]);
    printf("\n");
    printf("dot_count: %d\n", dot_count);
    printf("\n");
}
*/

inline const char *solve() {
    for (int i = 0; i < SIZE; i++) {
        if (X_row[i] == SIZE || X_col[i] == SIZE)
            return X_WON;
        if (O_row[i] == SIZE || O_col[i] == SIZE)
            return O_WON;
    }
    if (X_cross[0] == SIZE || X_cross[1] == SIZE)
        return X_WON;
    if (O_cross[0] == SIZE || O_cross[1] == SIZE)
        return O_WON;

    if (dot_count == 0)
        return DRAW;
    else
        return NOT_COMPLETE;
}

int main() {
    int T;

    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++) {
        clear_input();
        read_input();
        printf("Case #%d: %s\n", t, solve());
        //print_input();
    }
    return 0;
}
