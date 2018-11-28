#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    FILE *inp, *outp;
    int cases, i=1, n=0, in=0;
    float c, f, x;
    double time=0;
    inp=fopen("B-large.in","r");
    outp=fopen("output.txt","w");
    fscanf(inp,"%d",&cases);
    while(cases--)
    {
        fscanf(inp,"%f %f %f",&c,&f,&x);
        while(n<((x/c)-(2/f)-1))
            n++;
        while(in<n)
        {
            time=time+(1.0*c/(2.0+(1.0*f*in)));
            in++;
        }
        time=time+1.0*x/(2.0+(1.0*f*in));
        fprintf(outp,"Case #%d: %.7lf\n",i,time);
        i++;
        time=0;
        n=0;
        in=0;
    }
    fclose(inp);
    fclose(outp);
    return 0;
}
