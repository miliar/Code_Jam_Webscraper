#include<stdio.h>
#include<stdlib.h>
int main()
{
    FILE *fr, *fw;
    fr=fopen("B-large.in","r");
    fw=fopen("oup1.txt","w");
    int i,t;
    double c,f,x,sum,r;
    fscanf(fr,"%d",&t);
    for(i=0;i<t;i++)
    {
        sum=0;
        fscanf(fr,"%lf%lf%lf",&c,&f,&x);
        r=2.0;
        while(1)
        {
            if(((x-c)/r)<(x/(r+f)))
            {
                sum=sum+(x/r);
                break;
            }
            else
            {
                sum=sum+(c/r);
                r=r+f;
            }
        }
        fprintf(fw,"Case #%d: %.7lf",i+1,sum);
        if(i!=t-1)
            fprintf(fw,"\n");
    }
    fclose(fr);
    fclose(fw);
}
