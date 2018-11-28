#include <cstdio>
#include <cstring>
int T,row,x,h[20],ans;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    for (int tt = 0; tt < T; tt++)
    {
        memset(h, 0, sizeof h);
        for (int u = 0; u < 2; u++)
        {
            scanf("%d", &row);
            for (int i = 0; i < 4; i++)
                for (int j = 0; j < 4; j++)
                {
                    scanf("%d", &x);
                    if (i == row - 1) h[x]++;
                }
        }
        ans = -1;
        for (int i = 1; i <= 16; i++)
            if (h[i] == 2)
            {
                if (ans > 0) { ans = -2; break; }
                ans = i;
            }
        printf("Case #%d: ", tt + 1);
        if (ans == -1) printf("Volunteer cheated!\n");
        if (ans == -2) printf("Bad magician!\n");
        if (ans > 0) printf("%d\n", ans);
    }
    return 0;
}
