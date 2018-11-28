#include<stdio.h>
int main()
{
    int a[10][10],b[10][10],x,y,c,i,j,k,l,m,t,tc;
    scanf("%d",&tc);
    for(t=1;t<=tc;t++)
    {
        scanf("%d",&x);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&y);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&b[i][j]);

        c=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(a[x][i]==b[y][j])
                {
                    c++;
                    k=b[y][j];
                }
            }
        }
        if(c==0)
            printf("Case #%d: Volunteer cheated!\n",t);
        else if(c==1)
            printf("Case #%d: %d\n",t,k);
        else
            printf("Case #%d: Bad magician!\n",t);
    }
    return 0;
}
