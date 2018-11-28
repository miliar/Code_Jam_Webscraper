#include <iostream>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char * argv[]) {
    FILE* fpin = fopen("input.txt", "r");
    if (fpin == NULL) {
        fprintf(stderr, "No file\n");
        return -1;
    }
    FILE* fpout = fopen("output.txt", "w");
    if (fpin == NULL) {
        fprintf(stderr, "Cannot create file\n");
        return -1;
    }
    int T;
    fscanf(fpin, "%d", &T);
    
    for(int i = 0 ; i < T ; i++) {
        int X, R, C;
        fscanf(fpin, "%d %d %d", &X, &R, &C);
        if (R > C) {
            int t = R;
            R = C;
            C = t;
        }
        if (X == 1) {
            fprintf(fpout, "Case #%d: GABRIEL\n", i + 1);
        } else if (X == 2 && (R * C) >= X && ((R *C) % X == 0)) {
            fprintf(fpout, "Case #%d: GABRIEL\n", i + 1);
        } else if ( (X >= 7) || ((R * C) % X) || ((R * C) < X) ) {
            fprintf(fpout, "Case #%d: RICHARD\n", i + 1);
        } else {
            if (X == 3 && ((R == 2 && C == 3) || (R == 3 && C == 4) || (R == 3 && C == 3))) {
                fprintf(fpout, "Case #%d: GABRIEL\n", i + 1);
            } else if (X == 4 && (R >= 3) && (C == 4)) {
                fprintf(fpout, "Case #%d: GABRIEL\n", i + 1);
            }else {
                fprintf(fpout, "Case #%d: RICHARD\n", i + 1);
            }
        }
    }
    fclose(fpin);
    fclose(fpout);
    return 0;
}