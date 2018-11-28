#include<cstdio>
#include<cstdlib>
int main()
{
    int k=0,tc=0,i=0;
    double c,f,x,tmin,tk,tm,t=0.0,ck;
    scanf("%d",&tc);
    for(k=0;k<tc;k++)
    {
        t=0.0;ck=0;
        scanf("%lf %lf %lf",&c,&f,&x);
        tmin=x/2;
        ck=2;
        while(1)
        {
            t=t+c/ck;
            ck=ck+f;
            tk=t+x/ck;
            if(tk<tmin)
            {
                tmin=tk;
            }
            else
                break;
        }
        printf("Case #%d: %lf\n",k+1,tmin);
    }
    return 0;
}
