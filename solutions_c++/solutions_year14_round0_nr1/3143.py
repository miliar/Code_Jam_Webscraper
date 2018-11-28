// GCJ 2014 Qualification Round
// problem A

#include <iostream>
#include <cstdio>

using namespace std;

const int MAXN = 16;
const char input_file[] = "A.in", output_file[] = "A.out";

int main()
{
    int test_case, test_cur, res, i, j, target, row_test;
    int check[MAXN];

    FILE *fin = fopen(input_file, "r");
    FILE *fout = fopen(output_file, "w");

    fscanf(fin, "%d", &test_case);

    for (test_cur = 1; test_cur <= test_case; test_cur++)
    {

        for (i = 0; i < MAXN; i++)
            check[i] = 0;
        res = -1;

        for (row_test = 0; row_test < 2; row_test++)
        {
            fscanf(fin, "%d", &target);

            for (i = 0; i < 4; i++)
                for (j = 0; j < 4; j++)
                {
                    int x;
                    fscanf(fin, "%d", &x);
                    if (i + 1 == target)
                        check[x - 1]++;
                }
        }

        for (i = 0; i < MAXN; i++)
            if (check[i] == 2)
            {
                if (res == -1)
                    res = i + 1;
                else if (res > 0)
                    res = -2;
            }

        if (res == -1)
            fprintf(fout, "Case #%d: Volunteer cheated!\n", test_cur);
        else if (res == -2)
            fprintf(fout, "Case #%d: Bad magician!\n", test_cur);
        else
            fprintf(fout, "Case #%d: %d\n", test_cur, res);

    }

    fclose(fin);
    fclose(fout);

    return 0;
}



