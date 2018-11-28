#include<cstdio>
const double dx=1e-10;
int main()
{
    int T;
    scanf("%d",&T);
    for (int E=1;E<=T;E++)
    {
        double C,F,X;
        scanf("%lf%lf%lf",&C,&F,&X);
        double T_OneMoreFactory,T_NoMoreFactory;
        int n_factory=0;
        double answer=0.0;
        while(1)
        {
            T_NoMoreFactory=(X)/(2.0+((double)(n_factory))*F);
            T_OneMoreFactory=(X)/(2.0+((double)(n_factory+1))*F)+C/(2.0+((double)(n_factory))*F);
            if (T_NoMoreFactory-T_OneMoreFactory<dx)
                break;
            else
            {
                answer=answer+C/(2.0+((double)(n_factory))*F);
                n_factory++;
            }
        }
        printf("Case #%d: %.7lf\n",E,answer+T_NoMoreFactory);
    }
    return 0;
}
