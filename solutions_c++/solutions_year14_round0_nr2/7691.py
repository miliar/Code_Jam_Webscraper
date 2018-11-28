#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
   int t ,i;
   cin >>t ;
   double c,f,x,res,pres,factor,temp;

   for(i=1;i<=t;i++)
   {
     cin >> c ;
     cin >> f ;
     cin >> x ;
     res=x/(2.0);
     factor=(2.0);
     do{
      pres=res;
      res=res-(x/factor)+(c/factor);
      factor=f+factor;
      temp = res+(x/factor);
      res=temp;
     }while(res<pres);
  printf("Case #%d: %.7lf\n",i, pres);
   }
   
}
