#include<stdio.h>
#include<stdlib.h>

int magic1[4][4],magic2[4][4];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);

    int t, i, row1, row2;
    scanf("%d", &t);
    for(i=0; i<t; i++)
    {
        scanf("%d", &row1);
        int j, k;
        for(j=0; j<4; j++)
           for(k=0; k<4; k++)
            scanf("%d",&magic1[j][k]);
        scanf("%d", &row2);
        for(j=0; j<4; j++)
           for(k=0; k<4; k++)
            scanf("%d",&magic2[j][k]);
        int flag = 0, mark;
        for(j=0; j<4; j++)
           for(k=0; k<4; k++)
           {
               if(magic1[row1-1][j]==magic2[row2-1][k])
               {
                mark = magic1[row1-1][j];
                flag++;
               }
            }
        if(flag==1)
            printf("Case #%d: %d\n",i+1, mark);
        else
           if(flag>1)
              printf("Case #%d: Bad magician!\n",i+1);
           else
              printf("Case #%d: Volunteer cheated!\n",i+1);
    }
    return 0;
}
