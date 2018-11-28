#include <cstdio>
#include <cstdlib>
using namespace std;

long long mod;

long long log_multiplication(long long a, long long b)
{
    if (b < 8)
        return ((a * b) % mod);

    long long temp = (log_multiplication(a, b / 8) * 8) % mod;

    temp += ((a * (b % 8)) % mod);

    return (temp % mod);
}

long long quick_exponation(long long base, long long exponent)
{
    if (exponent == 0)
        return 1;

    if (exponent == 1)
        return base;

    long long temp = quick_exponation(base, exponent / 2);

    temp = log_multiplication(temp, temp);

    if (exponent % 2 == 1)
        temp = log_multiplication(temp, base);

    return temp;
}

bool witness(long long a)
{
    int k = __builtin_ctz(mod - 1);

    a = quick_exponation(a, (mod - 1) >> k);

    while (k--)
    {
        long long new_a = log_multiplication(a, a);

        if ((new_a == 1) and (a != 1) and (a != mod - 1))
            return 1;

        a = new_a;
    }

    return (a != 1);
}

bool miller_rabin_test(long long n, int s)
{
    if (n == 1)
        return 0;

    if (n < 4)
        return 1;

    mod = n;

    while (s--)
    {
        long long a = 1;

        while ((a == 1) or (a % 2 == 0))
            a = rand() % n;

        if (witness(a))
            return 0;
    }

    return 1;
}

void print_binary(int mask)
{
    for (int bit = 31 - __builtin_clz(mask); bit >= 0; bit--)
        printf("%d", (mask & (1 << bit)) ? 1 : 0);

    printf(" ");
}

long long interpretation[11];

long long get_interpretation(int mask, int base)
{
    long long exp = 1, res = 0;
    int s = 31 - __builtin_clz(mask);

    for (int bit=0; bit<=s; bit++, exp*=base)
    {
        if (mask & (1 << bit))
            res += exp;
    }

    return res;
}

void print_smallest_divisor(long long n)
{
    int i = 2;

    while (n % i)
        i++;

    printf("%d ", i);
}

int main()
{
    printf("Case #1:\n");

    int ctr = 0;

    for (int mask = (1 << 15); ctr < 50; mask++)
    {
        if (!(mask & 1))
            continue;

        bool is_jamcoin = 1;

        for (int i=2; i<=10; i++)
        {
            interpretation[i] = get_interpretation(mask, i);

            if (miller_rabin_test(interpretation[i], 100))
            {
                is_jamcoin = 0;
                break;
            }
        }

        if (!is_jamcoin)
            continue;

        print_binary(mask);

        for (int i=2; i<=10; i++)
            print_smallest_divisor(interpretation[i]);

        printf("\n");

        ctr++;
    }

    return 0;
}
