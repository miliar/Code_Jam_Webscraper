#include<stdio.h>
#include<string.h>
#include<stdlib.h>
double duration(double c,double f,double x,int n)
{
    double time=0;
    for(int j=0; j<n; j++)
    {
        time=time+(c/((j*f)+2));
    }
    time=time+(x/((n*f)+2));
    return time;
}
int main()
{
    FILE *file;
    file = fopen("B-small-attempt3.in","r");
    int cases,n,j;
    double time,c,f,x;
    fscanf(file,"%d",&cases);
    for(int i=0; i<cases; i++)
    {
        n=0;
        time=0;
        fscanf(file,"%lf %lf %lf",&c,&f,&x);
        for(j=1; j<10000; j++)
        {
            if((c*j)<=x)
                n++;
            else
                break;
        }
        if(n!=0)
        {
        for(j=0; j<=n-1; j++)
        {
            if(duration(c,f,x,j)<duration(c,f,x,j+1))
            {
                time=duration(c,f,x,j);
                break;
            }
            else if(j==n-1)
            {
                time=duration(c,f,x,j+1);
            }
        }
        }
        else
            time=x/(float)2;
        printf("Case #%d: %lf\n",i+1,time);
    }
    return 0;
}
