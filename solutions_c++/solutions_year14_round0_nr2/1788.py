#include <cstdio>
int main()
{
    int T;
    scanf("%d",&T);
    while (T--)
    {
        double C,F,X;
        scanf("%lf%lf%lf",&C,&F,&X);
        double best=1e100,now=0,rate=2;
        while (1)
        {
            if (now+X/rate<best)
                best=now+X/rate;
            else
                break;
            now+=C/rate;
            rate+=F;
        }
        static int id=0;
        printf("Case #%d: %.10f\n",++id,best);
    }
    return(0);
}

