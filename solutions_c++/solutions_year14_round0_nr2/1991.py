#include <stdio.h>
#include <math.h>

double calcst(int n,double c,double f,double x)
{
    double sum = 0;
    for(int i=0;i<n;i++)
    {
        sum += 1.0/(2.0+i*f);
        //printf("n=%-10d %-10.7f        %-10.7f\n",i+1,c*sum,2.0+(i+1)*f);
    }
    sum = c * sum + x/(2.0+n*f);
    return sum;
}

int main()
{
    int t;
    double c,f,x,ts;

    freopen ("B-large.in","r",stdin);
    freopen ("B-large.out","w",stdout);

    scanf("%d",&t);
    for (int i=1;i<=t;i++)
    {
        ts=0.0;
        scanf("%lf%lf%lf",&c,&f,&x);
        int n = floor(x/c - 2.0/f);
        //printf("c=%lf    f=%lf    x=%lf    n0=%d    n1=%d\n",c,f,x,n0,n1);

        if (n<1e-8)
        {
            printf("Case #%d: %.7f\n",i,x/2.0);
        }
        else
        {
            double ts = calcst(n,c,f,x);
            printf("Case #%d: %.7f\n",i,ts);
        }

    }

    fclose(stdout);
    fclose(stdin);

    return 0;
}
