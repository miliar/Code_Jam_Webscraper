#include <stdio.h>
#include <string.h>

int f[100][100];
int row_max[100];
int column_max[100];

int main()
{
    FILE * fin = fopen("B-large.in", "r");
    FILE * fout = fopen("B-large.out", "w");
    int i, j;
    int t, t_num = 1;
    int n, m;
    bool flag;

    fscanf(fin, "%d", &t);

    for (; t_num <= t; t_num++)
    {
        fscanf(fin, "%d%d", &n, &m);

        memset(row_max, 0, sizeof(row_max));
        memset(column_max, 0, sizeof(column_max));
        memset(f, 0, sizeof(f));

        for (i = 0; i < n; i++)
            for (j = 0; j < m; j++)
            {
                fscanf(fin, "%d", &f[i][j]);
                if ( f[i][j] > row_max[i] )
                    row_max[i] = f[i][j];
                if ( f[i][j] > column_max[j] )
                    column_max[j] = f[i][j];
            }

        flag = true;
        for (i = 0; i < n; i++)
        {
            for (j = 0; j < m; j++)
                if ( row_max[i] > f[i][j]  &&  column_max[j] > f[i][j] )
                {
                    flag = false;
                    break;
                }
            if ( !flag )
                break;
        }

        if ( flag )
            fprintf(fout, "Case #%d: YES\n", t_num);
        else
            fprintf(fout, "Case #%d: NO\n", t_num);
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
