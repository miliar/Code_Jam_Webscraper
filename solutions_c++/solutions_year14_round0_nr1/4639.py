#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int br[64];
int main()
{
    int t = 0, T;
    scanf("%d", &T);
    while(t++ < T)
    {
        int x;
        int i, j, tmp, br2 = 0, ans;
        memset(br, 0, sizeof(br));
        scanf("%d", &x);
        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++)
            {
                scanf("%d", &tmp);
                if(i == x)
                    br[tmp]++;
            }
        scanf("%d", &x);
        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++)
            {
                scanf("%d", &tmp);
                if(i == x)
                {
                    if(br[tmp])
                    {
                         br2++;
                         ans = tmp;
                    }
                    br[tmp]++;
                }
            }
        printf("Case #%d: ", t);
        if(br2 == 0)
        {
            printf("Volunteer cheated!\n");
        }
        else
        if(br2 == 1)
        {
            printf("%d\n", ans);
        }
        else
        {
            printf("Bad magician!\n");
        }
    }
    return 0;
}