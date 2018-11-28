#include <stdio.h>
#include <stdlib.h>

#define MAX 100

int main()
{
    int t;
    int n, m;
    int i, j, k, x, y;
    int L[MAX][MAX];
    int flag[MAX][MAX];
    int flag_ans, flag_row, flag_col;
    FILE *fp1, *fp2;

    fp1 = fopen("B-small-attempt1.in", "r");
    fp2 = fopen("output.txt", "w");
    if (!fp1 || !fp2)
        return 0;

    fscanf(fp1, "%d", &t);
    for (i = 0; i < t; i++)
    {
        flag_ans = 1; //Yes
        fscanf(fp1, "%d %d", &n, &m);
        for (j = 0; j < n; j++)
        {
            for (k = 0; k < m; k++)
            {
                fscanf(fp1, "%d", &L[j][k]);
            }
            flag[j][k] = 0;
        }
        if (m == 1 || n == 1)
        {
            fprintf(fp2, "Case #%d: YES\n", i + 1);
        }
        else
        {
            for (j = 0; j < n; j++)
            {
                for (k = 0; k < m; k++)
                {
                    if (L[j][k] == 1)
                    {
                        flag_row = 0;
                        flag_col = 0;
                        for (x = 0; x < m; x++)
                        {
                            if (L[j][x] > 1)
                                flag_row = 1;
                        }
                        for (y = 0; y < n; y++)
                        {
                            if (L[y][k] > 1)
                                flag_col = 1;
                        }
                        if (flag_row && flag_col)
                            flag_ans = 0; //No
                    }
                }
            }
            if (flag_ans)
            {
                fprintf(fp2, "Case #%d: YES\n", i + 1);
            }
            else
            {
                fprintf(fp2, "Case #%d: NO\n", i + 1);
            }
        }
    }
    fclose(fp1);
    fclose(fp2);
    return 0;
}
