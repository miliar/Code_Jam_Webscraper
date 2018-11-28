#include <stdio.h>
#include <iostream>>

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    int d[10000];

    for(int t = 0; t < T; ++t)
    {
        int S;
        scanf("%d", &S);
        char c = getchar();
        for(int s = 0; s <= S; ++s)
        {
            scanf("%c", &c);
            d[s] = c - '0';
        }
        c = getchar();
        int ans = 0, curr = d[0];
        for(int s = 1; s <= S; ++s)
        {
            if(curr < s)
            {
                ans += s - curr;
                curr += s - curr;
            }
            curr += d[s];

        }
        printf("Case #%d: %d\n", t + 1, ans);
    }
}
