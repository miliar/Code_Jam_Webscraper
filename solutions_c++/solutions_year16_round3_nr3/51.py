// vim:set sw=4 et smarttab:
// Round 1C 2016

#include <cstdio>

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        int a, b, c, z;
        scanf("%d%d%d%d", &a, &b, &c, &z);
        if (z > c)
            z = c;
        int answer[1000][3];
        int n_answer = 0;
        int combi_ik[10][10];
        int combi_jk[10][10];
        for (int i = 0; i < 10; ++i)
            for (int k = 0; k < 10; ++k)
                combi_ik[i][k] = 0;
        for (int j = 0; j < 10; ++j)
            for (int k = 0; k < 10; ++k)
                combi_jk[j][k] = 0;
        for (int i = 0; i < a; ++i)
        {
            int k = z * i;
            for (int j = 0; j < b; ++j)
            {
                int combi_ij = 0;
                for (int count = 0; count < c; ++count)
                {
                    if (combi_ij >= z)
                        continue;
                    if (combi_ik[i][k % c] >= z)
                        continue;
                    if (combi_jk[j][k % c] >= z)
                        continue;
                    ++combi_ij;
                    ++combi_ik[i][k % c];
                    ++combi_jk[j][k % c];
                    answer[n_answer][0] = i;
                    answer[n_answer][1] = j;
                    answer[n_answer][2] = k % c;
                    ++n_answer;
                    ++k;
                }
            }
        }
        printf("Case #%d: %d\n", tc, n_answer);
        for (int i = 0; i < n_answer; ++i)
            printf("%d %d %d\n", answer[i][0] + 1, answer[i][1] + 1, answer[i][2] + 1);
    }
}
