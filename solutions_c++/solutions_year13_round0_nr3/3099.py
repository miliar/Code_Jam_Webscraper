#include"stdio.h"
#include"math.h"
#include"string.h"
int x,y;
int palin(int num)
{
    int l;
    char str[1000];
    sprintf(str,"%d",num);
    l=strlen(str)-1;
    for(int i=0;i<=(l+1)/2-1;i++)
    {
        if(str[i]!=str[l-i])
            return 0;
    }

    return 1;
}
main()
{
    FILE *p1, *p2;
    int cas,c;
    double a,b;
    p1=fopen("C-small-attempt0.in","r");
    p2=fopen("ans0.in","w");
    fscanf(p1,"%d",&cas);
    for(int k=1;k<=cas;k++)
    {
        c=0;
        fscanf(p1,"%lf %lf",&a,&b);
        x=sqrt(a);
        if(x*x!=a)
            x++;
        y=sqrt(b);
        for(int i=x;i<=y;i++)
        {
            if(palin(i)==1)
            {
                c+=palin(i*i);
            }
        }
        fprintf(p2,"Case #%d: %d\n",k,c);
    }
}
