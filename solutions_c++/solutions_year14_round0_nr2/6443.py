#include<stdio.h>
double precision = 0.000001;
int main()
{
    FILE *input,*output;
    input= fopen("B-large.in","r");
    output=fopen("B-large.out","w");
    int t;
    fscanf(input,"%d",&t);
    int test;
    for(test=1;test<=t;test++)
    {
        double C,F,X;
        fscanf(input,"%lf %lf %lf",&C,&F,&X);
        double rate=2, time=0,cookies=0;
        while(X-cookies>precision)
        {
            //if(X-cookies >C)
            if( (C/rate + X/(rate+F)) < (X/rate)  )
            {
                time += C/rate;
                rate+= F;
                cookies=0;
            }
            else
            {
                //time += (X-cookies)/rate;
                time += X/rate;
                cookies=X;
            }//printf("time = %lf\n",time);
        }
        fprintf(output,"Case #%d: %.7lf\n",test,time);
    }
    return 0;
}
