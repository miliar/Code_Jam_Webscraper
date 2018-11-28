#include <stdio.h>
#include <string.h>
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-small-attempt.out","w",stdout);
    int t;
    long long n;
    scanf("%d",&t);
    int num[10];
    
    for (int cas = 1 ; cas <= t ; cas ++)
    {
        memset(num,0,sizeof(num));
        scanf("%lld",&n);
        int cou = 0,i;
        if ( n == 0)
        {
            printf("Case #%d: INSOMNIA\n",cas);
            continue;
        }
        for ( i = 1 ; i <= 1000000 ; i++ )
        {
            long long temp = n * i;
            while (temp)
            {
                if (num[temp % 10 ] != 1)
                {
                    cou ++;
                    num[temp % 10] = 1;
                }
                temp /= 10;
            }
            if ( cou == 10)
                break;
        }
        printf("Case #%d: %lld\n",cas,i * n);
    }
    return 0;
}