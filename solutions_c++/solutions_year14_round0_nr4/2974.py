// GCJ 2014 Qualification Round
// problem D

#include <iostream>
#include <cstdio>

using namespace std;


const char input_file[] = "D.in", output_file[] = "D.out";
const int MAXN = 1010;

int war(double* a, double *b, int n)
{
    int i, j, res = 0;
    bool *used_a = new bool[n], *used_b = new bool[n];

    for (i = 0; i < n; i++)
        used_a[i] = false, used_b[i] = false;

    for (i = 0; i < n; i++)
    {
        int biggest_a = -1, proper_b = -1, smallest_b = -1;
        for (j = 0; j < n; j++)
            if (!used_a[j] && (biggest_a < 0 || a[j] > a[biggest_a]))
                biggest_a = j;
        for (j = 0; j < n; j++)
            if (!used_b[j])
            {
                if (smallest_b < 0 || b[j] < b[smallest_b])
                    smallest_b = j;
                if (b[j] > a[biggest_a])
                    if (proper_b < 0 || b[j] < b[proper_b])
                        proper_b = j;
            }
        if (proper_b >= 0)
            res++, used_a[biggest_a] = true, used_b[proper_b] = true;
        else
            used_a[biggest_a] = true, used_b[smallest_b] = true;
    }

    delete[] used_a;
    delete[] used_b;
    used_a = NULL, used_b = NULL;
    return res;
}

int main()
{
    FILE *fin = fopen(input_file, "r");
    FILE *fout = fopen(output_file, "w");

    int test_case, test_cur, n, i;
    double naomi[MAXN], ken[MAXN];

    fscanf(fin, "%d", &test_case);

    for (test_cur = 1; test_cur <= test_case; test_cur++)
    {
        fscanf(fin, "%d", &n);

        for (i = 0; i < n; i++)
            fscanf(fin, "%lf", &(naomi[i]));

        for (i = 0; i < n; i++)
            fscanf(fin, "%lf", &(ken[i]));

        fprintf(fout, "Case #%d: %d %d\n", test_cur, war(ken, naomi, n), n - war(naomi, ken, n));
    }


    fclose(fin);
    fclose(fout);

    return 0;
}




