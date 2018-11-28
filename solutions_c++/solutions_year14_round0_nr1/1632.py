#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int map1[5][5];
int map2[5][5];
int flag1[17];
int flag2[17];
int main()
{
    FILE *fp = fopen("A-small-attempt0.in", "r");
    FILE *fo = fopen("output.out", "w");
    //FILE *fp = stdin;
    //FILE *fo = stdout;
    int t;
    int r1, r2;
    fscanf(fp, "%d", &t);
    for (int i = 1; i <= t; i++)
    {
        memset(flag1, 0, sizeof(flag1));
        memset(flag2, 0, sizeof(flag2));
        fscanf(fp, "%d", &r1);
        for (int j = 1; j <= 4; j++)
        {
            for (int k = 1; k <= 4; k++)
            {
                fscanf(fp, "%d", &map1[j][k]);
            }
        }
        fscanf(fp, "%d", &r2);
        for (int j = 1; j <= 4; j++)
        {
            for (int k = 1; k <= 4; k++)
            {
                fscanf(fp, "%d", &map2[j][k]);
            }
        }
        for (int j = 1; j <= 4; j++)
        {
            flag1[map1[r1][j]]++;
        }
        for (int j = 1; j <= 4; j++)
        {
            flag2[map2[r2][j]]++;
        }
        int ans = 0;
        int count = 0;
        for (int j = 1; j <= 16; j++)
        {
            if (flag1[j] > 0 && flag2[j] > 0)
            {
                ans = j;
                count++;
            }
        }
        if (count == 0)
        {
            fprintf(fo, "Case #%d: Volunteer cheated!", i);
        }
        else if (count > 1)
        {
            fprintf(fo, "Case #%d: Bad magician!", i);
        }
        else
        {
            fprintf(fo, "Case #%d: %d", i, ans);
        }
        fprintf(fo, "\n");
    }
    return 0;
}
