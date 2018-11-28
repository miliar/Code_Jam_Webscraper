#include<cstdio>

double sum[100];
int main()
{
    int t;
    double c,f,x;
    scanf("%d",&t);
    for(int tt=0;tt<t;tt++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        double t1=50000,t2=0,now=2,cc=0;
        t2=x/2;
        cc+=c/now;
        now+=f;
        while(t1>t2)
        {
            t1=t2;
            t2=cc+x/now;
            cc+=c/now;
            now+=f;
        }
        if(t1<t2) sum[tt]=t1;
        else sum[tt]=t2;
    }
    for(int i=0;i<t;i++)
    {
        printf("Case #%d: %.7lf\n",i+1,sum[i]);
    }
}
