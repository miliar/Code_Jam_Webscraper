#include<stdio.h>

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("correction.txt","w",stdout);
    int t,p;
    scanf("%d",&t);
    for(p=1;p<=t;p++)
    {
        int one,two,i,j;
        scanf("%d",&one);
        int temp[4][4];
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&temp[i][j]);
        scanf("%d",&two);
        int temp2[4][4];
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&temp2[i][j]);
        //printf("one %d two %d\n ",one,two);
        int k[8];
        for(i=0;i<4;i++)
            k[i]=temp[one-1][i];
        for(i=0;i<4;i++)
            k[i+4]=temp2[two-1][i];
        int p1=0,m=4,count=0,val;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                //printf("%d - %d =  %d\n",k[p1],k[m],k[p1]-k[m]);
                if(k[p1]-k[m++]==0){count++;val=k[p1];}
            }
            p1++,m=4;
        }
        if(count==0)printf("Case #%d: Volunteer Cheated!",p);
        else if(count==1)printf("Case #%d: %d",p,val);
        else printf("Case #%d: Bad magician!",p);
        printf("\n");
        //printf("count %d\n",count);
    }
    return 0;
}


