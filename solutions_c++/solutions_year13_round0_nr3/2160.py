#include<stdio.h>

bool palindrome(long long x)
{
    long long cur = x, y = 0;
    while (cur > 0)
    {
        y = y * 10 + cur % 10;
        cur /= 10;
    }
    return x == y;
}

int f(long long a)
{
    int num = 0;
    for (long long x = 1; x * x <= a; x++)
        if (palindrome(x) && palindrome(x*x))
            num++;
    return num;
}

int main()
{
//    freopen("B-large.in", "r", stdin);
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("cout.txt", "w", stdout);
    int T;
    long long a, b;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        scanf("%I64d%I64d", &a, &b);
        printf("Case #%d: %d\n", cas, f(b) - f(a-1));
    }
    return 0;
}
