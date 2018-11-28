#include<stdio.h>
#include<stdlib.h>

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int t, i;
    scanf("%d", &t);
    for(i=0; i<t; i++)
    {
        double c, f, x, time = 0.0000000;
        scanf("%lf %lf %lf", &c, &f, &x);
        if(c>=x)
            time = x/2;
        else
            {
             int num, j;
             num = int((f*x/c-2)/f);
             for(j=0; j<num; j++)
                 time += c/(2+j*f);
              time += x/(2+f*num);
            }
       printf("Case #%d: %.7lf\n",i+1, time);

    }
    return 0;
}


