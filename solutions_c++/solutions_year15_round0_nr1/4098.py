#include <cstdio>

int main()
{
    const int N = 1005;
    char shy[N];
    int t, s;
    scanf("%d", &t);
    for (int tst = 1; tst <= t; ++tst)
    {
        scanf("%d%s", &s, shy);
        int n = 0, sum = 0;
        for (int i = 0; i <= s; ++i)
        {
            n += i - sum;
            sum = i + shy[i] - '0';
        }
        printf("Case #%d: %d\n", tst, n);
    }
    return 0;
}
