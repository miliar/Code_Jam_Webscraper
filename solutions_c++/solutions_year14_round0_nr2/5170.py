#include<iostream>
#include<stdio.h>
using namespace std;
class cook
{
    double time;
    double rate;
     double c;
    double f;
    double x;
    public:
    cook()
    {
        rate=2.0;
        time=0.0;
    }
   void get_cfx()
   {
       cin>>c;
       cin>>f;
       cin>>x;
   }
    int compare()
    {
        double wt;
        double bt;
        wt=x/rate;
        bt=c/rate+x/(rate+f);
        if(bt<wt)
        {
            time=time+c/rate;

            rate=rate+f;
            return 1;
        }
        else
        {
         time=time+wt;
         return 0;
        }
    }
   double findtime()
    {
        while(compare());
        return time;
    }

};
int main()
{
 int n,n1,i=0;
 cin>>n;
 n1=n;
 cook p[n];
 while(n>0)
 {
     p[i].get_cfx();
     i++;
     n--;
 }
 i=0;
 while(n1>0)
 {

     printf("Case #%d: %.7f\n",i+1,p[i].findtime());
     n1--;
     i++;
 }
 return 0;
}
