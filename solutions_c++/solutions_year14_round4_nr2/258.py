#include <bits/stdc++.h>
using namespace std;

int a[1010];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &a[i]);
        }
        int l = 0, r = n - 1, ans = 0;
        while (l != r)
        {
            int pos = min_element(a + l, a + r + 1) - a;
            int move_l = pos - l;
            int move_r = r - pos;
            if (move_l <= move_r)
            {
                for (int i = pos; i > l; i--)
                {
                    a[i] = a[i - 1];
                }
                l++;
            }
            else
            {
                for (int i = pos; i < r; i++)
                {
                    a[i] = a[i + 1];
                }
                r--;
            }
            ans += min(move_l, move_r);
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
