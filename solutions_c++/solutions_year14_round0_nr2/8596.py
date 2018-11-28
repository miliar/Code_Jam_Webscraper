#include<stdio.h>

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("Blarge1.txt","w",stdout);
    int t,p;
    scanf("%d",&t);
    for(p=1;p<=t;p++)
    {
        double c,f,x;
        scanf("%lf %lf %lf",&c,&f,&x);
        //printf("%lf %lf %lf",c,f,x);

        double speed=2.0;
        double time_reqd=0.0;
        if(x<c)time_reqd = x/speed;
        else
        {
        while(((c/speed)+(x/(speed+f)))<(x/speed))
        {
            time_reqd+=(c/speed);
            speed+=f;
            //printf("%lf\n",time_reqd);
        }
        time_reqd+=x/speed;
        }
        printf("Case #%d: %0.7f\n",p,time_reqd);
    }
    return 0;
}


