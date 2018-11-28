#include <bits/stdc++.h>

int c[26];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("outLarge", "w", stdout);
    int T_T, __ = 0;
    scanf("%d", &T_T);

    while (T_T--)
    {
        printf("Case #%d:", ++__);
        int n;
        scanf("%d", &n);
        int  tot = 0;
        for (int i = 0; i < n; i++)
        {
            scanf("%d", c+i);
            tot += c[i];
        }
        int m = n;
        while (tot)
        {
            int p = n;
            int k = std::max_element(c, c + m) - c;
            putchar(' ');
            putchar('A' + k);
            c[k]--;
            tot--;
            if (c[k]==0) n--;
            if (p == 2 && tot)
            {

                int k = std::max_element(c, c + m) - c;
//                putchar(' ');
                putchar('A' + k);
                c[k]--;
                tot--;
                if (c[k]==0) n--;
            }
        }

        puts("");
    }


    return 0;
}
