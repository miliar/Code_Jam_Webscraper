#include <stdio.h>
#include <math.h>
double temp,anctemp;
double C,F,X;
int T;
int main()
{
    scanf(" %d",&T);
    for(int t = 1; t <= T; t++)
    {
        printf("Case #%d: ",t);
        scanf(" %lf %lf %lf",&C,&F,&X);
        long long int j = 0;
        temp = X/2;
        //printf("temp[%d] = %.7lf\n",j,temp[j]);
        if(X<=C)
            printf("%.7lf\n",temp);

        else
        {
            int numsteps = (X*F-2*C)/(C*F);
            double resp = X/(numsteps*F+2);
            for(int i = 0; i < numsteps; i++)
            {
                resp += C/(i*F+2);
            }

            printf("%.7lf\n",resp);

        }
    }
}
