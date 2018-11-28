#include <stdio.h>
#include <math.h>
#define error 10e-6

int main()
{
    int T;
    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        double C,F,X;
        double curSpeed=2;
        scanf("%lf %lf %lf",&C,&F,&X);
        double t = C/curSpeed;
        if(C > X)
        {
            printf("Case #%d: %.7lf\n",i+1,X/curSpeed);
        }
        else
        {
            double t1 = (X-C)/curSpeed;
            double t2 = X/(curSpeed+F);
            while(t1 > t2 )
            {
                curSpeed +=F;
                t += C/curSpeed;
                t1 = ( X-C )/curSpeed;
                t2 = X/(curSpeed+F);
            }
            printf("Case #%d: %.7lf\n",i+1,t+t1);
        }
    }
}