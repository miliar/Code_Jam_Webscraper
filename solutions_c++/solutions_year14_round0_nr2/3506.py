#include <stdio.h>

FILE *h,*g;

long t,i,j;
double c,f,x,precedent,curent,fabrici,biscuiti;

int main()
{
    h=fopen("prob2.in","r");
    g=fopen("prob2.out","w");

    fscanf(h,"%d",&t);

    for(i=1;i<=t;i++)
    {
        fabrici=0;
        precedent=999999;
        curent=0;
        biscuiti=2;
        fscanf(h,"%lf %lf %lf",&c,&f,&x);
        while (curent<=precedent)
        {
            curent=0;
            biscuiti=2;
            for (j=1;j<=fabrici;j++)
            {
                curent=curent+c/biscuiti;
                biscuiti+=f;
            }
            curent=curent+x/biscuiti;

            if (curent<precedent) precedent=curent;
            fabrici++;

        }
        fprintf(g,"Case #%d: %.10lf\n",i,precedent);

    }


    return 0;
}
