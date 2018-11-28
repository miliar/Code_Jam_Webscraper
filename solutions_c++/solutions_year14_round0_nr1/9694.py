#include<cstdio>
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,ii,ans_1,ans_2,tb1[4][4],tb2[4][4],num1[4],num2[4],intersection,i,j;
    scanf("%d",&t);
    for(ii=1;ii<=t;ii++)
    {
        scanf("%d",&ans_1);
        ans_1--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",tb1[i]+j);
            }
        }
        scanf("%d",&ans_2);
        ans_2--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",tb2[i]+j);
            }
        }
        for(i=0;i<4;i++)
        {
            num1[i]=tb1[ans_1][i];
        }
        for(i=0;i<4;i++)
        {
            num2[i]=tb2[ans_2][i];
        }
        intersection=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                intersection+=num1[i]==num2[j];
            }
        }
        printf("Case #%d: ",ii);
        if(intersection==0)
        {
            printf("Volunteer cheated!\n");
        }
        else if(intersection>1)
        {
            printf("Bad magician!\n");
        }
        else
        {
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                {
                    if(num1[i]==num2[j])printf("%d\n",num1[i]);
                }
            }
        }
    }
}
