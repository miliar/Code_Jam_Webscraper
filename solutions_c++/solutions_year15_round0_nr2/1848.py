#include <bits/stdc++.h>

using namespace std;

int a[2000], n, ans, T;

int main()
{
    freopen("in.in", "r", stdin);
    freopen("ou.out", "w", stdout);
    scanf("%d", &T);
    for (int itest = 0; itest < T; itest++)
    {
        scanf("%d", &n);
        ans = 0;
        for (int i = 0; i < n; i++) scanf("%d", &a[i]), ans += a[i];
        for (int  i = 1; i <= 1000; i++)
        {
            int res = 0;
            for (int j = 0; j < n; j++)
                if (a[j] > i) res += (a[j] - i) / i + (a[j] % i != 0) ;
            ans = min(ans, i + res);
        }

        printf("Case #%d: %d\n", itest + 1, ans);
    }

}
