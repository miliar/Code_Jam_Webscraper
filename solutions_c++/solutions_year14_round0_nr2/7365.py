#include<stdio.h>
#include<stdlib.h>
using namespace std;
int main()
{
    int t=0;
    scanf("%ld",&t);
     double p=2.0,s=0.0;

    for(int i=0;i<t;i++)
    {
        p=2.0;s=0.0;
          double C=0.0,F=0.0,X=0.0,tmin=0.0,tk=0.0;

        scanf("%lf %lf %lf",&C,&F,&X);
        tmin=X/p;
        while(1)
        {
            s=s+C/p;
            p=p+F;
            tk=s+X/p;
            if(tk<tmin)
            {
                tmin=tk;
            }
            else
            break;

        }


        printf("Case #%d: %.7lf\n",i+1,tmin);
    }
return 0;
}
