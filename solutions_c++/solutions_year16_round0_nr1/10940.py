#include <stdio.h>
long long int num[10]={0,};
long long int finder(long long int p)
{
    num[p%10]++;
    if (p/10 != 0) return finder(p/10);
    else return 0;
}
int main()
{
    long long int n, i,j, sum,t, T;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d", &T);
    for(i=1;i<=T;i++)
    {
        t=0;
        for(j=0;j<10;j++) num[j] = 0;
        scanf("%d", &n);
        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n",i);
            continue;
        }
        while(1)
        {
            t++;
            finder(n*t);
            sum=0;
            for(j=0;j<10;j++) if(num[j]!=0) sum++;
            if(sum == 10)
            {
                printf("Case #%d: %d\n",i, n*t);
                break;
            }
        }
    }
    return 0;
}
