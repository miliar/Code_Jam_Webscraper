/*
Your program should determine which card the volunteer chose;
    or if there is more than one card the volunteer might have chosen (the magician did a bad job);
    or if there's no card consistent with the volunteer's answers (the volunteer cheated).

Limits

1 <= T <= 100.
1 <= both answers <= 4.
Each number from 1 to 16 will appear exactly once in each arrangement. 
*/



#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <assert.h>
#include <string.h>


int T;

#define T_MAX 100

//#define MYDEBUG


FILE *fin;

void ReadData() {
    int i;
    int res;
    int row1, row2;

    int C1[4][4], C2[4][4];
    int r, c, c1, c2;
    int numDuplicates, duplicate;

    #define STRLEN_MAX 1000
    char str[STRLEN_MAX + 1];

    fgets(str, STRLEN_MAX, fin);
    sscanf(str, "%d", &T);
    //fscanf(fin, "%d", &T);

    assert(T >= 1 && T <= T_MAX);

    for (i = 0; i < T; i++) {
        /*
        fgets(str, STRLEN_MAX, fin);

        if (str[strlen(str) - 1] == '\n')
            str[strlen(str) - 1] = 0;
        if (str[strlen(str) - 1] == '\r')
            str[strlen(str) - 1] = 0;

        char *str1 = str;
        for (numBases = 0; ; numBases++) {
            res = sscanf(str1, "%d", &base[numBases]);
            if (res <= 0)
                break;
            assert(base[numBases] >= 2 && base[numBases] <= B_MAX);

            for (; ; str1++) {
                if (*str1 == ' ') {
                    str1++;
                    break;
                }
                    
                if (*str1 == 0)
                    break;
            }
        }
        assert(numBases >= 2 && numBases <= N_B_MAX);

        Solve(i + 1);
        fflush(stdout);
        */
        fscanf(fin, "%d", &row1);
        row1--;
        for (r = 0; r < 4; r++)
            for (c = 0; c < 4; c++)
                fscanf(fin, "%d", &C1[r][c]);

     #ifdef MYDEBUG
        for (r = 0; r < 4; r++) {
            for (c = 0; c < 4; c++)
                printf("%d ", C1[r][c]);
            printf("\n");
        }
        printf("%d\n\n", row1);
     #endif

        fscanf(fin, "%d", &row2);
        row2--;
        for (r = 0; r < 4; r++)
            for (c = 0; c < 4; c++)
                fscanf(fin, "%d", &C2[r][c]);

     #ifdef MYDEBUG
        for (r = 0; r < 4; r++) {
            for (c = 0; c < 4; c++)
                printf("%d ", C2[r][c]);
            printf("\n");
        }
        printf("%d\n\n", row2);
     #endif

        // Figure out the duplicates in the 2 rows:
        numDuplicates = 0;
        duplicate = -1;
        for (c1 = 0; c1 < 4; c1++)
            for (c2 = 0; c2 < 4; c2++) {
              #ifdef MYDEBUG
                printf("%d %d\n", C1[row1][c1], C2[row2][c2]);
              #endif
                if (C1[row1][c1] == C2[row2][c2]) {
                    duplicate = C1[row1][c1];
                    numDuplicates++;
                }
            }

      #ifdef MYDEBUG
        printf("numDuplicates = %d\n", numDuplicates);
      #endif

        assert((numDuplicates == 0) || (duplicate != -1));

        if (numDuplicates == 0)
            printf("Case #%d: Volunteer cheated!\n", i + 1);
        else if (numDuplicates == 1)
            printf("Case #%d: %d\n", i + 1, duplicate);
        else if (numDuplicates > 1)
            printf("Case #%d: Bad magician!\n", i + 1);
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
