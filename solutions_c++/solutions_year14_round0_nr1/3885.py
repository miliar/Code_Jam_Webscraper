#include<stdio.h>

int main()
{
    int t,p,q,a[4][4],b[4][4];
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
        int s=0,count=0;
        scanf("%d",&p);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        scanf("%d",&q);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&b[i][j]);
            }
        }
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(a[p-1][i]==b[q-1][j])
                {
                    s=a[p-1][i];
                    count++;
                }
            }
        }
        printf("Case #%d: ",k);
        if(count==0)
            printf("Volunteer cheated!\n");
        if(count==1)
            printf("%d\n",s);
        if(count>1)
            printf("Bad magician!\n");
    }

}
