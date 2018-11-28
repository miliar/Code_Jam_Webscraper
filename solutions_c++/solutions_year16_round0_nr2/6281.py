#include <bits/stdc++.h>

char buffer[128];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T_T, __ = 0;
    scanf("%d", &T_T);

    while (T_T--)
    {
        scanf("%s", buffer);
        char c = buffer[0];
        int cnt = 0;
        for (int i = 1; buffer[i]; i++) if (c != buffer[i])
        {
            cnt++;
            c = buffer[i];
        }
        if (c == '-') cnt++;
        printf("Case #%d: %d\n", ++__, cnt);
    }


    return 0;
}
