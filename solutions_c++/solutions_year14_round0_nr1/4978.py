#include<stdio.h>
int sum[20];
int main()
{
    //freopen("fun.in", "r", stdin);
    freopen("fun.out", "w", stdout);
    int T;
    int a,b,temp;
    int i,j,flag,k,n,m;
    scanf("%d",&T);
    //printf("*T* %d\n",T);
    for (k = 1; k <=T; ++k)
    {
        for (i = 0; i < 20; ++i)
        {
            sum[i]=0;
        }
        for(n=0; n<2; n++)
        {
            scanf("%d",&a);
            //printf("*a* %d\n",a);
            for(m=1; m<5; m++)
            {
                //printf("*m*%d \n",m);
                if(m==a)
                {
                    for (i = 0; i < 4; ++i)
                    {
                        scanf("%d",&b);
                        sum[b]++;
                        // printf(" %d",b);
                    }
                    //printf("\n");
                }
                else
                {
                    for (i = 0; i < 4; ++i)
                    {
                        scanf("%d",&temp);
                    }
                }
            }
        }
        flag=0;
        for (i = 1; i < 17; ++i)
        {
            if(sum[i]>1)
            {
                j=i;
                flag++;
            }
        }
        if(flag==0)
        {
            printf("Case #%d: Volunteer cheated!\n",k);
        }
        else if(flag==1)
        {
            printf("Case #%d: %d\n",k,j);
        }
        else
        {
            printf("Case #%d: Bad magician!\n",k);
        }
    }
    return 0;
}
