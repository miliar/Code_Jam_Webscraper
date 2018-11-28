#include<stdio.h>

int main()
{
    int t,k;
    int arr[5][5];
    int cache[5] = {0};
    scanf("%d",&t);
    for(k=1; k<=t; k++)
    {
        int i,j,q1,q2,cards = 0,flag,m;
        scanf("%d",&q1);
        for(i=1; i<=4; i++)
            for(j=1; j<=4; j++)
            scanf("%d", &arr[i][j]);
        for(i=1; i<=4; i++)
            cache[i] = arr[q1][i];
        scanf("%d",&q2);
        for(i=1; i<=4; i++)
            for(j=1; j<=4; j++)
            scanf("%d", &arr[i][j]);
        for(i=1; i<=4; i++)
        {
            flag = 0;
            for(j=1; j<=4 && flag == 0; j++)
            {
                if(arr[q2][i] == cache[j])
                {
                    m = j;
                    flag = 1;
                }
            }
            if(flag == 1)
                cards++;
        }
        printf("Case #%d: ",k);
        if(cards == 0)
            printf("Volunteer cheated!");
        else if(cards == 1)
            printf("%d",cache[m]);
        else
            printf("Bad magician!");
        printf("\n");
    }
    return 0;
}
