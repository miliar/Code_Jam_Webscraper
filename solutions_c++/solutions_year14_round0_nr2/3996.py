#include <iostream>
#include <cstdio>
#include <math.h>
using namespace std;

FILE *pfile;
FILE *pfile2;

int main()
{
    pfile = fopen ("myfile.txt","r");
    pfile2= fopen ("myfile2.txt","w");
    int t;
    int p=1;
    fscanf(pfile,"%d",&t);
    while (p<=t)
    {
        double c,f,x;
        double seconds=0;
        double rate = 2;
        fscanf(pfile,"%lf%lf%lf",&c,&f,&x);
        {
            while(1)
            {
                double temp = c / rate;
                if(x/rate < c / rate)
                {
                    seconds =x/rate;
                    break;
                }
                else if((x-c)/rate < x/(rate + f)  )
                {
                    seconds += temp + (x-c)/rate ;
                    break;
                }
                else
                {
                    rate +=f;
                    seconds+=temp ;
                }
            }
            fprintf(pfile2,"Case #%d: %.7lf\n",p,seconds);
            p++;
        }

    }
}
