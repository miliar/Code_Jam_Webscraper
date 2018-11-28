#include <stdlib.h>
#include <stdio.h>

char data[4][5];

char * judge() {
    int counterX_V[4] = { 0 };
    int counterX_H[4] = { 0 };
    int counterO_V[4] = { 0 };
    int counterO_H[4] = { 0 };
    int counterX_D_A[9] = { 0 };
    int counterX_D_S[9] = { 0 };
    int counterO_D_A[9] = { 0 };
    int counterO_D_S[9] = { 0 };

    int counterDot = 0;
    for (int x = 0; x < 4; x++) {
        for (int y = 0; y < 4; y++) {
            if (data[y][x] == 'X' || data[y][x] == 'T') {
                counterX_H[y]++;
                counterX_V[x]++;
                counterX_D_A[y+x]++;
                counterX_D_S[y-x+4]++;
            }
            if (data[y][x] == 'O' || data[y][x] == 'T') {
                counterO_H[y]++;
                counterO_V[x]++;
                counterO_D_A[y+x]++;
                counterO_D_S[y-x+4]++;
            }
            if (data[y][x] == '.') {
                counterDot++;
            }
        }
    }
    for (int i = 0; i < 4; i++) {
        if (counterX_H[i] == 4 || counterX_V[i] == 4) {
            return "X won";
        }
        if (counterO_H[i] == 4 || counterO_V[i] == 4) {
            return "O won";
        }
    }
    if (counterX_D_A[3] == 4) {
        return "X won";
    }
    if (counterO_D_A[3] == 4) {
        return "O won";
    }

    if (counterX_D_S[4] == 4) {
        return "X won";
    }
    if (counterO_D_S[4] == 4) {
        return "O won";
    }
    if (counterDot == 0) {
        return "Draw";
    } else {
        return "Game has not completed";
    }
}
int main()
{
    FILE *in = fopen("e:\\codejam\\in.txt", "rw");
    FILE *out = fopen("e:\\codejam\\out.txt", "w");
    int n = 0;
    fscanf(in, "%d", &n);
    for (int caseIndex = 0; caseIndex < n; caseIndex++) {
        for (int i = 0; i < 4; i++) {
            fscanf(in, "%s", data[i]);
        }
        fprintf(out, "Case #%d: ", caseIndex + 1);
        fprintf(out, "%s\n", judge());
    }
    return 0;
}
