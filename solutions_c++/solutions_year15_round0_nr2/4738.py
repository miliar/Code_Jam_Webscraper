#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
using namespace std;
const int maxN = 	1005;
int ca, n, ans;
int a[maxN];
int main()
{
    scanf("%d", &ca);
    int t = 0;
    while (ca--)
    {
        ++t;
        scanf("%d", &n);
        for (int i = 1; i <= n; ++i)
            scanf("%d", a + i);
        
        ans = 2147483647;
        
        for (int i = 1; i <= 1000; ++i)
        {
            int tmp = 0;
            for (int j = 1; j <= n; ++j)
                if (a[j] > i)
                {
                    tmp += a[j] / i - 1;
                    if (a[j] % i) tmp++;
                }
            ans = min(ans, tmp + i);
        }
        
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}

