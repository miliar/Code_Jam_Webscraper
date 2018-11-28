#include <iostream>
#include <stdio.h>

using namespace std;

bool check(int a)
{
    while (a > 1)
    {
        if (a%2 != 0) return false;
        a /= 2;
    }
    return true;
}

int main()
{
    int n, ii;
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.txt", "w", stdout);
    cin>>n;
    for (ii = 1; ii <= n; ++ii)
    {
        int a, b;
        scanf("%d/%d", &a, &b);
        if (a <= 0 || a > b)
        {
            printf("Case #%d: impossible\n", ii);
            continue;
        }
        if (b%a == 0)
        {
            b /= a;
            a = 1;
        }
        if (check(b) == false)
        {
            printf("Case #%d: impossible\n", ii);
            continue;
        }
        int ans = 0;
        while (a < b)
        {
            ans ++;
            b /= 2;
        }
        printf("Case #%d: %d\n", ii, ans);
    }
    return 0;
}
