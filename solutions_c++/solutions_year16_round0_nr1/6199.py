#include <bits/stdc++.h>

bool vis[10];
int cnt;

inline void bits(long long k)
{
    while (k != 0)
    {
        if (!vis[k % 10])
        {
            vis[k % 10] = true;
            cnt++;
        }
        k /= 10;

    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T_T, __ = 0;
    scanf("%d", &T_T);

    while (T_T--)
    {
        int n;
        scanf("%d", &n);
        if (n == 0)
        {
            printf("Case #%d: INSOMNIA\n", ++__);
            continue;
        }
        memset(vis, 0, sizeof vis);
        cnt = 0;
        long long k = n;
        bits(k);
        while (cnt != 10)
        {
            k += n;
            bits(k);
//            printf("%I64d %d\n", k, cnt);
//            system("pause");
        }
        printf("Case #%d: %I64d\n", ++__, k);
    }

    return 0;
}
