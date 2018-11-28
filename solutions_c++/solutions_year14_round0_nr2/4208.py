#include <stdio.h>
#include <math.h>
#include <sched.h>

long double solve(long double C, long double F, long double X)
{
    int n = ceil( (X*F - 2*C) / (F * C) - 1 );
    
    long double s = 0;

    if (n<0)
    {
        n = 0;
    }

    for (int i=0;i<n;++i)
    {
        s+=C/(F*i + 2);
    }
    s += X / (F*n + 2);

    return s;
}

int main()
{
    struct sched_param param;
    param.sched_priority = 99;
    sched_setscheduler(0, SCHED_FIFO, &param);
    
    int T;
    scanf("%d", &T);
    long double C;
    long double F;
    long double X;
    
    for (int i=0;i<T;++i)
    {
        scanf("%Lf %Lf %Lf", &C, &F, &X);
        
        printf("Case #%d: %.7Lf\n", i+1, solve(C, F, X));
    }
}
