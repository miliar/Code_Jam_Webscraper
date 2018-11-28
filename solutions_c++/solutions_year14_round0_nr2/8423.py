#include<stdio.h>
int main()
{

    int T,i;
    double C,F,X,tm,rt,t1,t2;
    FILE *p1,*p2;
    p1=fopen("B-large.in","r");
     p2=fopen("output2","w");
    fscanf(p1,"%d",&T);
    for(i=1;i<=T;i++)
    {
        tm=t1=t2=0;
        rt=2;
        fscanf(p1,"%lf",&C);
        fscanf(p1,"%lf",&F);
        fscanf(p1,"%lf",&X);
        while(1)
        {
            t1=tm+X/rt;
            tm+=C/rt;
            rt+=F;
            t2=tm+X/rt;
            if(t2>t1)
             break;
        }
        //tm=tm+X/rt;
        fprintf(p2,"Case #%d: %.7lf\n",i,t1);
    }
    fclose(p1);
    fclose(p2);
    return 0;
}
