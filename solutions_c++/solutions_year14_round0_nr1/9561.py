//bansal0301
#include<stdio.h>
//#include<algorithm>
int main()
{
    int n,i,j,t,k,a[5][5]={0},ans1,ans2,ans[5];
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d",&ans1);
        for(i=1;i<5;i++)
        {
            for(j=1;j<5;j++)
            {
                scanf("%d",&a[i][j]);
                if(ans1==i)
                {
                    ans[j]=a[i][j];
                }
            }
        }
        scanf("%d",&ans2);
        for(i=1;i<5;i++)
        {
            for(j=1;j<5;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        int flag=0;
            for(i=1;i<5;i++)
            {
                for(j=1;j<5;j++)
                {
                   if(a[ans2][i]==ans[j])
                   {
                    flag++;
                    n=ans[j];
                   }
                }
            }
        if(flag==0)
        {
            printf("Case #%d: Volunteer cheated!\n",k);
        }
        else if(flag==1)
        {
            printf("Case #%d: %d\n",k,n);
        }
        else
        printf("Case #%d: Bad magician!\n",k);
    }
return 0;
}
