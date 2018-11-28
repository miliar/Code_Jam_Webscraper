#include<stdio.h>
main()
{
    int t;
    scanf("%d",&t);
    long long int p, q, tm;
    char x;
    for(int i = 1; i <=t; i++)
    {

        scanf("%lld%c%lld",&p,&x,&q);
        tm = q/p;
        int cnt = 1;
        int flag = 0;
        long long int d = 1;
        double z = double(p)/double(q);
        while(z < 0.5)
        {
            cnt++;
            z *= 2.0;
        }
        //printf("%lld/%lld\n",p,q);
        if(tm * p == q)
        {

        while(1)
            {
                if(tm == d )
                {
                    flag = 1;
                    break;
                }
                else if(d > tm)
                {
                    flag = 0;
                    break;
                }
                d <<= 1;

            }
        }
            if(flag == 0)
            {
                tm = q;
                d = 1;
               while(1)
            {
                if(tm == d )
                {
                    flag = 1;
                    break;
                }
                else if(d > tm)
                {
                    flag = 0;
                    break;
                }
                d <<= 1;

            }
            }

        printf("Case #%d: ",i);
        if(flag)
            printf("%d\n",cnt);
        else
            printf("impossible\n");

    }
}
