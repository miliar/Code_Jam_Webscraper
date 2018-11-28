// vim:set sw=4 et smarttab:
// Qualification Round 2016

#include <cstdio>

int get_bit_set(int n)
{
    int ret = 0;
    while (n > 0)
    {
        ret |= (1 << n % 10);
        n /= 10;
    }
    return ret;
}

int solve(int n)
{
    if (n == 0)
        return -1;
    int set = 0, in = n;
    while (true)
    {
        set |= get_bit_set(in);
        if (set == (1 << 10) - 1)
            break;
        in += n;
    }
    return in;
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        int n;
        scanf("%d", &n);
        int answer = solve(n);
        printf("Case #%d: ", tc);
        if (answer >= 0)
            printf("%d\n", answer);
        else
            printf("INSOMNIA\n");
    }
}
