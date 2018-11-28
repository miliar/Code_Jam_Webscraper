#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int a[100000];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int q = 0; q < t; ++q)
    {
        printf("Case #%d: ", q + 1);

        int n, x;
        scanf("%d%d", &n, &x);
        for (int i = 0; i < n; ++i)
            scanf("%d", &a[i]);
        sort(a, a + n);
        int ans = 0;
        int r = n - 1;
        int l = 0;
        while (l <= r)
        {
            if (a[l] + a[r] <= x)
                l++;
            r--;
            ans++;
        }
        printf("%d\n", ans);
    }
    return 0;

}
