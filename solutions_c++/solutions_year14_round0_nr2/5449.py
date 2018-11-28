#include<stdio.h>
double C,F,X;
int main()
{
    int t,T;
    scanf("%d",&T);
    double Ans,Min,get;
    for(t=1;t<=T;t++)
    {
        scanf("%lf %lf %lf",&C,&F,&X);
        Ans=0; get=2; Min=X/2;
        for(;;)
        {
            Ans+=C/get;
            get+=F;

            if(Min<Ans+X/get) break;
            Min = Ans+X/get;
        }
        printf("Case #%d: %.7lf\n",t,Min);
    }
}
