#include <stdio.h>

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,i=1;
    scanf("%d",&t);
    while(t--)
    {
        double tr=1,time=0,hu=2,inter1,inter,c,f,x;
        scanf("%lf %lf %lf",&c,&f,&x);
        inter1=(x/hu);
        //printf("%lf\n",inter1);
        while(tr)
        {
        inter=time+(x/(hu+f))+(c/hu);
        //printf("%lf\n",inter);
        if(inter>inter1)
        {tr=0;}
        else
        {inter1=inter;time=time+(c/hu);hu=hu+f;}
        }
        printf("Case #%d: %.7lf\n",i,inter1);
        i++;
    }
    return 0;
}
