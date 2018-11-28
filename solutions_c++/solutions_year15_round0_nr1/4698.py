#include <stdio.h>

int main()
{
    int T;
    freopen("A-large.in", "r", stdin);
    freopen("Output.out", "w", stdout);
    scanf("%d", &T);

    for(int loop = 1; loop <= T; loop++)
    {
        int Smax;
        scanf("%d", &Smax);
        int S[3000];

        char c;
        for(int i = 0; i <= Smax; i++)
        {
            scanf("%c", &c);
            if(c < '0') scanf("%c", &c);
            S[i] = c - '0';
        }

        int now_stand = S[0];
        int add = 0;
        for(int i = 1; i <= Smax; i++)
        {
            if(S[i] > 0)
            {
                if(now_stand >= i) now_stand += S[i];
                else
                {
                    add += i - now_stand;
                    now_stand += S[i] + i - now_stand;
                }
            }
        }

        printf("Case #%d: %d\n", loop, add);
    }
}
