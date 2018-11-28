#include <stdio.h>
int main()
{
    freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
    int t,te;
    scanf("%d",&t);
    for(te=1;te<=t;te++)
    {
        double c,sf=2,f,x,time=0,i;
        scanf("%lf %lf %lf",&c,&f,&x);
        if(x<c)time=x/sf;
        else
        {
            for(i=c;;i=c)
            {
                //printf("%f %f %f %f\n",c/sf,(x-i)/sf,x/(sf+f),time);
                time+=c/sf;
                if((x-i)/sf<x/(sf+f)){time+=(x-i)/sf;break;}
                sf+=f;
            }
        }
        printf("Case #%d: %.7f\n",te,time);
    }
    return 0;
}
