
#include<stdio.h>
int T,caz,i,n,x,sol,sum;
char c;
int main()
{

    freopen("date.in","r",stdin);
    freopen("date.out","w",stdout);
    scanf("%d",&T);
    while(T)
    {
        caz++;
        scanf("%d ",&n);
        for(i=0;i<=n;i++)
        {

            scanf("%c ",&c);
            x=c-'0';
            if(sum<i)
            {

                sol+=(i-sum);
                sum=i;
            }
            sum+=x;

        }
        printf("Case #%d: %d\n",caz,sol);
        sol=0;
        sum=0;
        T--;
    }
    return 0;

}
