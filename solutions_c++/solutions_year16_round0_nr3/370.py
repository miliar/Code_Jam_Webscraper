// vim:set sw=4 et smarttab:
// Qualification Round 2016

#include <cstdio>
#include <cstring>
#include <cassert>
#include <vector>

__int128 exp_table[11][32];

__int128 my_power(int a, int b)
{
    __int128 ret = 1;
    for (int i = 0; i < b; ++i)
        ret *= a;
    return ret;
}

__int128 parse_number(const char number[], int base)
{
    int len = strlen(number);
    __int128 n = 0;
    for (int i = 0; i < len; ++i)
    {
        int digit = number[len - 1 - i] - '0';
        n += my_power(base, i) * digit;
    }
    return n;
}

bool verify(const char number[], const int factors[])
{
    for (int base = 2; base <= 10; ++base)
    {
        __int128 n = parse_number(number, base);
        int f = factors[base - 2];
        if (f <= 1 || f == n || n % f != 0)
        {
            //fprintf(stderr, "ERROR number = %s, base = %d, parsed %lld factor = %d\n", number, base, n, f);
            //parse_number(number, base);
            return false;
        }
    }
    return true;
}

int factor(int n, int bit_set, int base)
{
    __int128 number = 1;
    for (int i = 0; i < n - 2; ++i)
        if (bit_set & (1 << i))
            number += exp_table[base][i + 1];
    number += exp_table[base][n - 1];
    if (number % 2 == 0)
        return 2;
    //for (__int128 i = 3; i * i <= number; i += 2)
    for (int i = 3; i < 1000000; i += 2)
        if (number % i == 0)
            return i;
    return 1;
}

void print(int n, int bit_set, const int factors[])
{
    char number[32 + 1];
    number[n] = '\0';
    number[0] = '1';
    for (int i = 1; i < n - 1; ++i)
        number[i] = '0';
    number[n - 1] = '1';
    for (int i = 0; i < n - 2; ++i)
        if (bit_set & (1 << i))
            number[n - 2 - i] = '1';
    assert(verify(number, factors));
    printf("%s", number);
    for (int i = 0; i < 9; ++i)
        printf(" %d", factors[i]);
    printf("\n");
}

int main()
{
    for (int base = 2; base <= 10; ++base)
    {
        exp_table[base][0] = 1;
        for (int i = 1; i < 32; ++i)
            exp_table[base][i] = exp_table[base][i - 1] * base;
    }
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        int n, j;
        scanf("%d%d", &n, &j);
        printf("Case #%d:\n", tc);
        for (int bit_set = 0; j > 0 && bit_set != (1 << (n - 2)) - 1; ++bit_set)
        {
            int factors[9];
            bool flag = true;
            for (int base = 2; base <= 10; ++base)
            {
                int t = factor(n, bit_set, base);
                if (t == 1)
                {
                    flag = false;
                    break;
                }
                factors[base - 2] = t;
            }
            if (flag)
            {
                --j;
                print(n, bit_set, factors);
            }
        }
    }
}
