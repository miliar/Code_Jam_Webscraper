#include <stdio.h>
#define eps 1e-9

int main ()
{
    double C,F,X,fac,A,B,can;
    int t,kase=0;
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);

    scanf ("%d",&t);

    while (t--){
        scanf ("%lf %lf %lf",&C,&F,&X);
        can=2.0;
        A=X/can;
        fac=C/can;
        can+=F;
        B=fac+(X/can);

        while (A+eps>=B){
            A=B;
            fac=fac+(C/can);
            can+=F;
            B=fac+X/can;
        }

        printf ("Case #%d: %.7lf\n",++kase,A);
    }
    return 0;
}
