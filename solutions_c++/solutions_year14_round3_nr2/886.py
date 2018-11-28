// GCJ 2014 Qualification Round 1C
// problem A

#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int MAX_LENGTH = 100;

int main()
{
    FILE *fin = fopen("A.in", "r");
    FILE *fout = fopen("A.out", "w");

    int test_case, test_now, i, j;
    long long p, q;

    fscanf(fin, "%d", &test_case);

    for (test_now = 1; test_now <= test_case; test_now++)
    {
        char s[MAX_LENGTH];
        fscanf(fin, "%s", s);

        p = q = 0;

        for (i = 0; i < strlen(s); i++)
            if (s[i] == '/')
                break;
            else
            {
                long long num_bit = (s[i] - '0');
                long long ten = 10;
                p = p * ten + num_bit;
            }

        j = i;
        for (i = j + 1; i < strlen(s); i++)
        {
            long long num_bit = (s[i] - '0');
            long long ten = 10;
            q = q * ten + num_bit;
        }

        long long one_ll = 1;
        long long two_fourty = (one_ll << 40);
        long long a = (p * two_fourty);

        if (a % q != 0)
            fprintf(fout, "Case #%d: impossible\n", test_now);
        else
        {
            long long x = a / q;
            int ans = 0;
            while (x > 0)
            {
                ans++;
                x = (x >> 1);
            }
            fprintf(fout, "Case #%d: %d\n", test_now, 41 - ans);
        }

    }

    fclose(fin);
    fclose(fout);

    return 0;
}

