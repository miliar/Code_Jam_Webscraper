#include <algorithm>
#include <cstdio>

/* Google Code Jam Round 2 2014
 * Problem A. Data Packing
 * Solution in C++
 * By Smithers
 */

int main()
{
    int t, ti;
    
    std::scanf("%d", &t);
    for (ti = 1; ti <= t; ti++)
    {
        int n, x;
        std::scanf("%d%d", &n, &x);
        int s[10000];
        for (int i = 0; i < n; i++)
            std::scanf("%d", &s[i]);
        std::sort(s, s+n);
        int ans = 0;
        for (int i = 0, j = n-1; i <= j; )
        {
            if (s[i] + s[j] <= x)
                i++;
            j--;
            ans++;
        }
        std::printf("Case #%d: %d\n", ti, ans);
    }
    return 0;
}
