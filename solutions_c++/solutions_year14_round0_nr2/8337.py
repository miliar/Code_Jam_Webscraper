#include <bits/stdc++.h>
using namespace std;


int main()
{
    int t;
    int i ,j,t1;
    double c,f,x;
    scanf("%d",&t);
    t1=0;
    while(t--)
    {
        t1++;
        scanf("%lf %lf %lf",&c,&f,&x);
        double ans=0.0;
        double inc=2.0;

        double new_inc;

        while(1)
        {
            double tmp1,tmp2,tmp3;
            new_inc=(inc+f);
            tmp1= x/inc;
            tmp2=c/inc;
            tmp3=x/new_inc;

            double mini=min(tmp1,tmp2+tmp3);
            if(tmp1==mini)
            {
                ans+=tmp1;
                break;
            }
            else
            {
                ans+=tmp2;
                inc=new_inc;
            }


        }

        printf("Case #%d: %.7lf\n",t1,ans);

    }

    return 0;
}
