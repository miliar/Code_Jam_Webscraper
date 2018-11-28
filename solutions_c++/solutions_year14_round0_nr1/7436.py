#include<stdio.h>

int main()
{
    int A[5][5],B[5][5],c,ans1,ans2,t,i,loc;
    //freopen("A-small-attempt5.in","r",stdin);
    //freopen("A-small-attempt5.out","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        c=0;
        scanf("%d",&ans1);
        for(int k=0;k<4;k++)
        {
            for(int h=0;h<4;h++)
                scanf("%d",&A[k][h]);
        }
        scanf("%d",&ans2);
        for(int k=0;k<4;k++)
        {
            for(int h=0;h<4;h++)
                scanf("%d",&B[k][h]);
        }
        for(int k=0;k<4;k++)
        {
            for(int h=0;h<4;h++)
            {
                if(A[ans1-1][k]==B[ans2-1][h])
                {
                    loc=A[ans1-1][k];
                    c++;
                }
            }
        }
        if(c==1)
            printf("Case #%d: %d\n",i,loc);
        else if(c==0)
            printf("Case #%d: Volunteer cheated!\n",i);
        else
            printf("Case #%d: Bad magician!\n",i);
    }
    return 0;
}
