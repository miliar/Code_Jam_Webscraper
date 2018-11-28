#include<stdio.h>
int main()
{
    int t;
    double c,f,x,s,time;
    int i;
    freopen("H:B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
         scanf("%lf%lf%lf",&c,&f,&x);
        s=2;
        time=0;
        while(x/s>x/(s+f)+c/s)
        {
            time+=c/s;
            s+=f;
        }
        time+=x/s;
        printf("Case #%d: ",i);
        printf("%.7lf\n",time);
    }
    return 0;
}
