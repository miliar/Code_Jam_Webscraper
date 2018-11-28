#include<cstdio>

int mycount[30],sum,n,t;

int main()
{
    freopen("A-large (2).in","r",stdin);
    freopen("eq.out","w",stdout);
    scanf("%d",&t);
    for(int round=1;round<=t;round++)
    {
        sum = 0;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&mycount[i]);
            sum += mycount[i];
        }
        printf("Case #%d: ",round);
        while(sum > 0)
        {
            int max1 = 1;
            int max2 = 0;
            for(int i=2;i<=n;i++)
            {
                if(mycount[i] > mycount[max1])
                {
                    max2 = max1;
                    max1 = i;
                }
                else if(mycount[i] >= mycount[max2])
                {
                    max2 = i;
                }
            }
            if(sum == 2)
            {
                printf("%c%c",max1+64,max2+64);
                break;
            }
            else if(mycount[max2] > (sum-2)/2)
            {
                bool q = true;
                for(int i=1;i<=n;i++)
                {
                    if(i == max1 || i == max2)
                        continue;
                    if(mycount[i] > (sum-2)/2)
                        q = false;
                }
                if(q)
                {
                    mycount[max1]--;
                    sum--;
                    printf("%c%c ",max1+64,max2+64);
                    mycount[max2]--;
                    sum--;
                }
                else
                {
                    mycount[max1]--;
                    sum--;
                    printf("%c ",max1+64);
                }
            }
            else if(mycount[max1] >= 2)
            {
                printf("%c%c ",max1+64,max1+64);
                mycount[max1]-=2;
                sum-=2;
            }
            else if(mycount[max1] == 1)
            {
                printf("%c ",max1+64);
                mycount[max1]-=1;
                sum-=1;
            }
        }
        printf("\n");
    }
}
