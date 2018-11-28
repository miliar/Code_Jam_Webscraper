#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

void printMatrix(FILE * g, int slides[][50], int B){
    for(int j = 0; j < B; j++){
        for(int k = 0; k < B; k++){
            fprintf(g, "%d", slides[j][k]);
        }
        fprintf(g, "\n");
    }
}

int main()
{
    FILE *f, *g;
    //f = fopen("input", "r");
    //g = fopen("output", "w");
    f = stdin;
    g = stdout;

    int T, B;
    unsigned long long M;
    int i, j, k;
    int slides[50][50];

    for(j = 0; j < 50; j++){
        for(k = 0; k < 50; k++){
            slides[j][k] = 0;
        }
    }

    fscanf(f, "%d ", &T);

    for(i = 1; i <= T; i++){
        fscanf(f, " %d %llu", &B, &M);

        for(k = 0; k < 50; k++){
            slides[0][k] = 0;
        }

        for(j = 1; j < 50; j++){
            for(k = j+1; k < 50; k++){
                slides[j][k] = 1;
            }
        }

        fprintf(g, "Case #%d: ", i);

        if(M > (1 << B-2)){
            fprintf(g, "IMPOSSIBLE\n", i);
            continue;
        }

        if(M == (1 << B-2)){
            fprintf(g, "POSSIBLE\n", i);
            for(j = B-1; j > 0; j--){
                slides[0][j] = 1;
            }
            printMatrix(g, slides, B);
            continue;
        }

        for(j = B-2; j >= 0; j--){
            slides[0][j] = M % 2;
            M >>= 1;
        }

        fprintf(g, "POSSIBLE\n");
        printMatrix(g, slides, B);
    }

    fclose(f);
    fclose(g);
    return 0;
}
