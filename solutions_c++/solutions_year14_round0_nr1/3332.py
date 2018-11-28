#include<stdio.h>
int a1[5][5];
int a2[5][5];
int c1[5];
int c2[5];
int main()
{
    #ifndef ONLINE_JUDGE
        freopen("input.c","r",stdin);
        freopen("output.c","w",stdout);
    #endif // ONLINE_JUDGE
    int t,i,index;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        int j,ans1,ans2,count=0;
        scanf("%d",&ans1);
        for(j=0;j<5;j++)
        {
            c1[j]=c2[j]=0;
        }
        for(j=1;j<=4;j++)
        {
            scanf("%d %d %d %d",&a1[j][1],&a1[j][2],&a1[j][3],&a1[j][4]);
        }
        scanf("%d",&ans2);
        for(j=1;j<=4;j++)
        {
            scanf("%d %d %d %d",&a2[j][1],&a2[j][2],&a2[j][3],&a2[j][4]);
        }
        int l=0;
        for(j=1;j<=4;j++)
        {
            count=0;
            int k;
            for(k=1;k<=4;k++)
            {
                if(a1[ans1][j]==a2[ans2][k])
                {
                    count++;
                }
            }
            if(count>0)
            {
                c1[l]=count;
                c2[l]=j;
                l++;
            }
        }
        count=0;
        for(j=0;j<l;j++)
        {
            if(c1[j]!=0)
            {
                count++;
                index=j;
            }
        }
        printf("Case #%d: ",i);
        if(count==0)
        {
            printf("Volunteer cheated!\n");
        }
        else if((count==1)&&(c1[index]==1))
        {
            printf("%d\n",a1[ans1][c2[index]]);
        }
        else
        {
            printf("Bad magician!\n");
        }
    }
    return 0;
}
