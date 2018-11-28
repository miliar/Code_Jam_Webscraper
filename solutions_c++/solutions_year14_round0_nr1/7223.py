#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

main()
{
    int T, i, a, b, c, j, p1[5][5], p2[5][5], ans, num=0, v;
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("out", "w", stdout);
    scanf("%d", &T);
    while(T--)
    {
        scanf("%d", &a);
        for(i=1; i<=4; i++)
        {
            for(j=1; j<=4; j++)
            {
                scanf("%d", &p1[i][j]);
            }
        }
        scanf("%d", &b);
        for(i=1; i<=4; i++)
        {
            for(j=1; j<=4; j++)
            {
                scanf("%d", &p2[i][j]);
            }
        }
        ans=0;
        for(i=1; i<=4; i++)
        {
            for(j=1; j<=4; j++)
            {
                if(p1[a][i]==p2[b][j])
                {
                    ans++;
                    v=p1[a][i];
                }
            }
        }
        printf("Case #%d: ", ++num);
        if(ans==1)
        {
            printf("%d\n", v);
        }
        else if(ans==0)
        {
            printf("Volunteer cheated!\n");
        }
        else
        {
            printf("Bad magician!\n");
        }
    }

    return 0;
}
