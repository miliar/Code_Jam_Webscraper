#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("answer.txt", "w", stdout);
    int t,n,tem;
    int num[20];
    scanf("%d", &t);
    for(int i = 1; i <= t; i++)
    {
        memset(num, 0, sizeof(num));
        for(int j = 0; j < 2; j++)
        {
            scanf("%d", &n);
            for(int k = 1; k <= 4; k++)
                for(int p = 1; p <= 4; p++)
                {
                    scanf("%d", &tem);
                    if(k == n) num[tem]++;
                }
        }
        tem = 0;
        int flag;
        for(int j = 1; j <= 16; j++)
            if(num[j] == 2)
            {
                tem++;
                flag = j;
            }
        printf("Case #%d: ", i);
        if(!tem) printf("Volunteer cheated!\n");
        else if(tem == 1) printf("%d\n", flag);
        else printf("Bad magician!\n");
    }
    return 0;
}
