#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t = 0;
    scanf("%d", &t);
    vector <double> a, b;
    for (int T = 0; T < t; T++)
    {
        printf("Case #%d: ", T + 1);
        int n;
        scanf("%d", &n);
        a.resize(n);
        b.resize(n);
        for (int i = 0; i < n; i++)
            scanf("%lf", &a[i]);
        for (int i = 0; i < n; i++)
            scanf("%lf", &b[i]);

        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        int l = 0;
        int r = 0;
        int ans1 = 0;
        while (l < n)
        {
            while (r < n && b[r] < a[l])
                r++;
            if (r < n)
            {
                ans1++;
                r++;
            }
            l++;
        }
        ans1 = n - ans1;

        l = 0;
        r = 0;
        int ans2 = 0;
        while (r < n)
        {
            while (l < n && a[l] < b[r])
                l++;
            if (l < n)
            {
                ans2++;
                l++;
            }
            r++;
        }

        printf("%d %d\n", ans2, ans1);
    }

    return 0;
}
