/*
From https://code.google.com/codejam/contest/2974486/dashboard#s=p1

Your program should determine which card the volunteer chose;
    or if there is more than one card the volunteer might have chosen (the magician did a bad job);
    or if there's no card consistent with the volunteer's answers (the volunteer cheated).

Limits

1 <= T <= 100.
Small dataset

1 <= C <= 500.
1 <= F <= 4.
1 <= X <= 2000.
Large dataset

1 <= C <= 10000.
1 <= F <= 100.
1 <= X <= 100000.
*/



#include <stdio.h>
#include <assert.h>
#include <string.h>


int T;

#define T_MAX 100

//#define MYDEBUG


FILE *fin;

void ReadData() {
    int i, numFarms, j;
    double C, F, X;
    double delta, timeToX, crtRate;

    #define STRLEN_MAX 1000
    char str[STRLEN_MAX + 1];

    //fgets(str, STRLEN_MAX, fin);
    //sscanf(str, "%d", &T);
    fscanf(fin, "%d", &T);
    #ifdef MYDEBUG
    printf("T=%d\n", T);
    #endif

    assert((T >= 1) && (T <= T_MAX));

    for (i = 0; i < T; i++) {
        fscanf(fin, "%lf%lf%lf", &C, &F, &X);
      #ifdef MYDEBUG
        printf("C, F, X = %lf %lf %lf\n", C, F, X);
      #endif

        timeToX = X / 2.0;
        numFarms = int((F * X - 2 * C) / (F * C));
        for (; ; numFarms++) {
          #ifdef MYDEBUG
            printf("numFarms = %d\n", numFarms);
          #endif
            delta = numFarms + (2 * C - F * X) / (F * C);

          #ifdef MYDEBUG
            printf("delta = %.3f\n", delta);
          #endif

            if (delta > 0.0)
                break;


            timeToX = 0.0;
            crtRate = 2.0;
            for (j = 0; j < numFarms; j++) {
                timeToX += C / crtRate;
                crtRate += F;
            }
            timeToX += X / crtRate;

          #ifdef MYDEBUG
            printf("timeToX = %.7f\n", timeToX);
          #endif
        }

        printf("Case #%d: %.7f\n", i + 1, timeToX);
    }
}


int main() {
    //freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A.in", "rt", stdin);
    /*
    freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A-large.in", "rt", stdin);
    freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A-large.out", "wt", stdout);
    */
    //freopen("A-large-practice.in", "rt", stdin);
    //freopen("A-large-practice.out", "wt", stdout);

    fin = stdin;
    ReadData();

    fclose(fin);

    return 0;
}
