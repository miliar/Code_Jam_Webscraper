#include <cstdio>

using namespace std;

int main()
{
 freopen("B-large.in","r",stdin);
  freopen("B-large-attempt0.out","w",stdout);
    int t,no=1;
    scanf("%d",&t);
    while(t--)
    {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        double time=0.0;
        double cokies=0.0,produc=2.0;
        while(cokies<x)
        {
                    double t1=(x-cokies)/produc,t2=(c-cokies)/produc,t3=(x-cokies+c)/(produc+f);

            if(cokies>=c&&t3<t1)
            {
                produc+=f;
                cokies-=c;

            }
            t1=(x-cokies)/produc;
            t2=(c)/produc;

            if(t1<=t2)
            {
                time+=t1;
                cokies=x;
            }
            else
            {
                time+=t2;
                cokies+=c;
            }
             //       printf("%lf COOKIE:%lf T1: %lf   T2: %lf\n",time,cokies,t1,t2);

        }
        printf("Case #%d: %.7lf\n",no++,time);
    }

    return 0;
}
