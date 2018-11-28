#include <stdio.h>

main(){

int T, row, t, i, j;
int posible[4];
int res;

scanf("%d", &T);
for(int caso=1;caso<=T;caso++)
{
    scanf("%d", &row);
    for(i=1;i<row;i++)
        for(j=0;j<4;j++) scanf("%d", &t);
    for(i=0;i<4;i++)
        scanf("%d", &posible[i]);
    for(i=0;i<4-row;i++)
        for(j=0;j<4;j++) scanf("%d", &t);

    scanf("%d", &row);
    for(i=1;i<row;i++)
        for(j=0;j<4;j++) scanf("%d", &t);
    for(res=i=0;i<4;i++)
    {
        scanf("%d", &t);
        for(j=0;j<4;j++)
        {
            if( posible[j] == t && res == 0 )
                res = t;
            else if( posible[j] == t && res != 0 )
                res = -1;
        }
    }
    for(i=0;i<4-row;i++)
        for(j=0;j<4;j++) scanf("%d", &t);

    printf("Case #%d: ", caso);
    if( res > 0 )
        printf("%d\n", res);
    else if( res == -1 )
        printf("Bad magician!\n");
    else if( res == 0 )
        printf("Volunteer cheated!\n");
}

return 0;
}

