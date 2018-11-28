// google code jam 2013 Qualification Round
// problem B

#include <iostream>
#include <cstdio>
using namespace std;

const int MAXN = 110;

int height[MAXN][MAXN], max_height_row[MAXN], max_height_column[MAXN];
int m, n;

int main()
{
    FILE *fin = fopen("B.in", "r");
    FILE *fout = fopen("B.out", "w");
    int test_t;
    bool res;
    fscanf(fin, "%d", &test_t);
    for (int testcase = 1; testcase <= test_t; testcase++)
    {
        fscanf(fin, "%d%d", &n, &m);
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++)
                fscanf(fin, "%d", &(height[i][j]));
        for (int i = 1; i <= n; i++)
        {
            max_height_row[i] = 0;
            for (int j = 1; j <= m; j++)
                max_height_row[i] = height[i][j] > max_height_row[i] ? height[i][j] : max_height_row[i];
        }
        for (int j = 1; j <= m; j++)
        {
            max_height_column[j] = 0;
            for (int i = 1; i <= n; i++)
                max_height_column[j] = height[i][j] > max_height_column[j] ? height[i][j] : max_height_column[j];
        }
        res = true;
        for (int i = 1; res && i <= n; i++)
            for (int j = 1; res && j <= m; j++)
                if (height[i][j] < max_height_column[j] && height[i][j] < max_height_row[i])
                    res = false;
        if (res)
            fprintf(fout, "Case #%d: YES\n", testcase);
        else
            fprintf(fout, "Case #%d: NO\n", testcase);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
