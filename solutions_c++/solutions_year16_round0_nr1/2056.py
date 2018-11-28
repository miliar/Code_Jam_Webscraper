#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int flag;

void mark(int x)
{
    while (x > 0)
    {
        int last = x%10;
        flag = flag | (1 << last);
        x /= 10;
    }
}

int main()
{
    int test;
    long long n;
    //freopen("test.in", "r", stdin);
    //freopen("test.out", "w", stdout);
    scanf("%d", &test);
    for (int t = 1; t <= test; t++)
    {
        flag = 0;
        scanf("%lld", &n);
        int i = 1;
        if (n == 0)
        {
            printf("Case #%d: INSOMNIA\n", t);
            continue;
        }
        while (flag != 1023)
        {
            long long x = n*i;
            mark(x);
            i++;
        }
        printf("Case #%d: %lld\n", t, n*(i-1));
    }
    return 0;
}
