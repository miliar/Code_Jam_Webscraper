#include <bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    int val = (1 << 10) - 1;
    for (int nc = 1; nc <= tc; nc++)
    {
        printf("Case #%d: ", nc);
        int t;
        scanf("%d", &t);
        if (t == 0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        int cur = 0;
        int c = 0;
        do
        {
            cur += t;
            int x = cur;
            while (x > 0)
            {
                c |= (1 << (x % 10));
                x /= 10;
            }
        } while ((c & val) != val);
        printf("%d\n", cur);
    }
}
