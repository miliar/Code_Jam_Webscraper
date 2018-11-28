#include<iostream>
#include<fstream>
#include <iomanip>

using namespace std;
fstream f1,f2;



int main()
{  f1.open("large.in",ios::in);
   f2.open("out.out",ios::out);
   double c,x,f,n,time,a,b,d,e,tt;
   int cas,count=0;
   f1>>cas;
   while(cas)
   {
       cas--;
       count++;
       f1>>c>>f>>x;
       n=2;
       tt=0;
       while(1)
       {
           a=x/n;
           b=c/n;
           n=n+f;
           d=x/n;
           e=b+d;
           if(a<e)
           {
               time=a+tt;
               break;
           }
           else
           tt=tt+b;

       }

       f2<<"Case #"<<count<<": "<<setprecision(10)<<time<<"\n";

   }
   return 0;
}
