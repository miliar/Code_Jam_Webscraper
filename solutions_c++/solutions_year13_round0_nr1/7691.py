#include <stdio.h>
#include <stdlib.h>

#define MAX 4

int main()
{
    int n_test;
    int i = 0, j = 0, k = 0, x, y;
    char T[MAX+1][MAX+1], T1[MAX+1][MAX+1], T2[MAX+1][MAX+1];
    //char temp;
    int flag_dot = 0;
    int flag_won = 0;
    FILE *fp1, *fp2;

    //fp1 = fopen("input.txt", "r");
    fp1 = fopen("A-small-attempt2.in", "r");
    fp2 = fopen("output.txt", "w");
    if (!fp1 || !fp2)
        return 0;

    fscanf(fp1, "%d\n", &n_test);
    //scanf("%d\n", &n_test);

    for (i = 0; i < n_test; i++)
    {
        flag_dot = 0;
        flag_won = 0;
        for (j = 0; j < MAX; j++)
        {
            for (k = 0; k < MAX; k++)
            {
                fscanf(fp1, "%c", &T[j][k]);
                //scanf("%c", &T[j][k]);
                T1[j][k] = T[j][k];
                T2[j][k] = T[j][k];
                //fprintf(fp2, "%c", TT[j][k]);
                //printf("%c", TT[j][k]);
                if (T[j][k] == 'T')
                {
                    T1[j][k] = 'X';
                    T2[j][k] = 'O';
                }
                if (T[j][k] == '.')
                {
                    flag_dot = 1;
                }
            }
            //getchar();
            //printf("\n");
            //scanf("\n");
            fscanf(fp1, "\n");
            //fprintf(fp2, "\n");
        }

        if (T1[0][0] == 'X' && T1[1][1] == 'X' && T1[2][2] == 'X' && T1[3][3] == 'X')
        {
            //printf("X won\n");
            if (!flag_won)
            {
                fprintf(fp2, "Case #%d: X won\n", i + 1);
                flag_won = 1;
            }
        }
        if (T2[0][0] == 'O' && T2[1][1] == 'O' && T2[2][2] == 'O' && T2[3][3] == 'O')
        {
            //printf("O won\n");
            if (!flag_won)
            {
                fprintf(fp2, "Case #%d: O won\n", i + 1);
                flag_won = 1;
            }
        }
        if (T1[3][0] == 'X' && T1[2][1] == 'X' && T1[1][2] == 'X' && T1[0][3] == 'X')
        {
            //printf("X won\n");
            if (!flag_won)
            {
                fprintf(fp2, "Case #%d: X won\n", i + 1);
                flag_won = 1;
            }
        }
        if (T2[3][0] == 'O' && T2[2][1] == 'O' && T2[1][2] == 'O' && T2[0][3] == 'O')
        {
            //printf("O won\n");
            if (!flag_won)
            {
                fprintf(fp2, "Case #%d: O won\n", i + 1);
                flag_won = 1;
            }
        }
        for (j = 0; j < MAX; j++)
        {
            if (T1[j][0] == 'X' && T1[j][1] == 'X' && T1[j][2] == 'X' && T1[j][3] == 'X')
            {
                //printf("X won\n");
                if (!flag_won)
                {
                    fprintf(fp2, "Case #%d: X won\n", i + 1);
                    flag_won = 1;
                }
            }
            else if (T1[0][j] == 'X' && T1[1][j] == 'X' && T1[2][j] == 'X' && T1[3][j] == 'X')
            {
                //printf("X won\n");
                if (!flag_won)
                {
                    fprintf(fp2, "Case #%d: X won\n", i + 1);
                    flag_won = 1;
                }
            }
        }
        for (j = 0; j < MAX; j++)
        {
            if (T1[j][0] == 'O' && T1[j][1] == 'O' && T1[j][2] == 'O' && T1[j][3] == 'O')
            {
                //printf("O won\n");
                if (!flag_won)
                {
                    fprintf(fp2, "Case #%d: O won\n", i + 1);
                    flag_won = 1;
                }
            }
            else if (T1[0][j] == 'O' && T1[1][j] == 'O' && T1[2][j] == 'O' && T1[3][j] == 'O')
            {
                //printf("O won\n");
                if (!flag_won)
                {
                    fprintf(fp2, "Case #%d: O won\n", i + 1);
                    flag_won = 1;
                }
            }
        }
        if (!flag_won)  //nobody win
        {
            if (flag_dot)  //has dot
                fprintf(fp2, "Case #%d: Game has not completed\n", i + 1);
            //printf("Unfinish\n");
            else
                fprintf(fp2, "Case #%d: Draw\n", i + 1);
            //printf("Draw\n");
        }
        fscanf(fp1, "\n");
    }
    fclose(fp1);
    fclose(fp2);
    return 0;
}
