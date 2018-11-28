#include <stdio.h>

using namespace std;

int main()
{
    int t;
    float c,f,x;
    int count=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%f %f %f",&c,&f,&x);

        double time=0.0,t1,t2,rate=2.0,target=0.0;

        while(target != x)
        {
            t1=x/rate;
            t2=c/rate + x/(rate+f);

            if(t1<t2)
            {
                target=x;
                time+=t1;
            }
            else
            {
                time+=c/rate;
                rate+=f;
            }
        }
        printf("Case #%d: %0.7f\n",count,time);
        count++;


    }
}
