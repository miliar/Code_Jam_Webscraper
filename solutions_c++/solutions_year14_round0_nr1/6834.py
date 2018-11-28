#include<stdio.h>

int main()
{
    int tests,t,a1,a2;
    scanf("%d",&tests);

    int a[4][4];
    int p1[4],p2[4];

    for(t=1;t<=tests;t++)
    {
        scanf("%d",&a1);
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            scanf("%d",&a[i][j]);

        for(int j=0;j<4;j++)
            p1[j]=a[a1-1][j];

        scanf("%d",&a2);
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            scanf("%d",&a[i][j]);

        for(int j=0;j<4;j++)
            p2[j]=a[a2-1][j];

        int ctr=0,pos;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            if(p1[i]==p2[j])
            {
                ctr++;
                pos=i;
            }
        if(ctr==1)
            printf("Case #%d: %d\n",t,p1[pos]);
        else if(ctr==0)
            printf("Case #%d: Volunteer cheated!\n",t);
        else
            printf("Case #%d: Bad magician!\n",t);
    }
    return 0;
}
