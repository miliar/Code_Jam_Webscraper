// GCJ 2014 Qualification Round 1B
// problem A

#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int MAX_LENGTH = 110, MAXN = 100;

int main()
{
    FILE *fin = fopen("A.in", "r");
    FILE *fout = fopen("A.out", "w");

    int test_case, test_now;
    int i, j, k, ans, n, s_compressed_length[MAXN], s_mul[MAXN][MAX_LENGTH];
    char s[MAX_LENGTH], s_compressed[MAXN][MAX_LENGTH];
    bool check;

    fscanf(fin, "%d", &test_case);

    for (test_now = 1; test_now <= test_case; test_now++)
    {
        fscanf(fin, "%d", &n);
        for (i = 0; i < n; i++)
        {
            fscanf(fin, "%s", s);
            s_compressed_length[i] = 0;
            for (j = 0; j < strlen(s); j++)
                if (j == 0 || s[j] != s[j - 1])
                {
                    s_compressed[i][s_compressed_length[i]++] = s[j];
                    s_mul[i][s_compressed_length[i] - 1] = 1;
                }
                else
                    s_mul[i][s_compressed_length[i] - 1]++;
            s_compressed[i][s_compressed_length[i]] = '\0';
        }

        check = true;
        for (i = 0; check && i < n; i++)
            if (strcmp(s_compressed[i], s_compressed[0]) != 0)
                check = false;

        if (!check)
        {
            fprintf(fout, "Case #%d: Fegla Won\n", test_now);
            continue;
        }

        ans = 0;
        for (i = 0; i < s_compressed_length[0]; i++)
        {
            int opt_min = MAX_LENGTH + 10;
            for (j = 0; j < n; j++)
            {
                int opt_cnt = 0;
                for (k = 0; k < n; k++)
                    opt_cnt += (s_mul[k][i] > s_mul[j][i] ? s_mul[k][i] - s_mul[j][i] : s_mul[j][i] - s_mul[k][i]);
                if (opt_cnt < opt_min)
                    opt_min = opt_cnt;
            }
            ans += opt_min;
        }

        fprintf(fout, "Case #%d: %d\n", test_now, ans);

    }

    fclose(fin);
    fclose(fout);
    return 0;
}
