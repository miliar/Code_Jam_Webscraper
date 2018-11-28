#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("b.txt","r",stdin);
    freopen("b_out.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for (int a=0; a<tc; a++)
    {
        double c,f,x,r,t,tt,tmp1,tmp2;
        scanf("%lf%lf%lf",&c,&f,&x);
        r=2;
        t=x/r;
        tt=0;
        while (t*f>c)
        {
              tmp1=tt;
              tmp2=t;
              tt+=c/r;
              r+=f;
              t=x/r;
              if (t*f<=c)
              {
                 tt=tmp1;
                 t=tmp2;
                 break;
              }
        }
        printf("Case #%d: %.7lf\n",a+1,tt+t);
    }
}
