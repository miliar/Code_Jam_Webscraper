#include<stdio.h>


using namespace std;

int main()
{
    double c, f, x;
    int t,te=1;
    freopen("B-large.in ","r",stdin);
    scanf("%d",&t);
    while(te<=t)
    {
          double tme = 0.0,rate = 2.0,ctime=0.0,xtime=0.0,xnext=0.0;



          scanf("%lf%lf%lf",&c,&f,&x);
          while(1)
          {
                 ctime = (double)c/rate;
                 xtime = (double)x/rate;
                 xnext =(double)x/(rate+f);
                 if((double)(xnext+ctime)>(double)xtime)
                 {
                     tme = (double)tme + (double)xtime;

                     break;
                 }
                 rate = (double)rate + (double) f;
                 tme = (double)tme + (double)ctime;

          }
          printf("Case #%d: %0.7lf\n",te,tme);
          te++;


    }
    return 0;
}
