#include<stdio.h>
int main()
{
    int t,cas=1;
    double c,f,x,now,time;

    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        now=2,time=0;
        while(1)
        {
            if(x/now>c/now+x/(now+f))
            {
                time+=c/now;
                now+=f;
            }
            else break;
        }
        time+=x/now;
        printf("Case #%d: %.7f\n",cas++,time);
    }

    return 0;
}
