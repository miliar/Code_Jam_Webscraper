#include <stdio.h>

int main()
{
    int t,i;
    double r,c,f,x,T;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        r=2;T=0;
        scanf("%lf %lf %lf",&c,&f,&x);
        while(x/r > ((c/r) + (x)/(r+f)))
        {
        //    printf(" %f + ",c/r);
            T += c/r;
            //x -= c;
            r += f;
        }
        T += x/r;
       // printf(" %f = ",x/r);
        printf("Case #%d: %.7f\n",i,T);
    }
    return 0;
}
