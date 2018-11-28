#include<stdio.h>
int main()
{
    int a[4][4],b[4][4];
    int t,aa,bb,i,j,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d",&aa);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        }
        scanf("%d",&bb);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                scanf("%d",&b[i][j]);
        }
        int count[17]={0};
        for(i=0;i<4;i++)
        {
            count[a[aa-1][i]]++;
        }
        for(i=0;i<4;i++)
        {
            count[b[bb-1][i]]++;
        }
        int counter=0,ci;
        for(i=1;i<17;i++)
        {
            if(count[i]>1)
            {
                counter++;
                ci=i;
            }
        }
        if(counter==1)
            printf("Case #%d: %d\n",k,ci);
        else if(counter>1)
            printf("Case #%d: Bad magician!\n",k);
        else
            printf("Case #%d: Volunteer cheated!\n",k);
    }
    return 0;
}
