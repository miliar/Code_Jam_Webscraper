#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
  int T;
  cin>>T;
  int flag=1;
  while(T--)
  {
      double C,F,X;
      cin>>C>>F>>X;
      double k=2;
      double sum=0;
      double m=X/C;



      while(1)
      {

         if((C/k*m)>(C/k+(C/(k+F))*m))
         {
             sum+=C/k;
             k=k+F;
         }
         else
        break;


      }
      sum+=C/k*m;
      printf("Case #%d: %.7f\n",flag,sum);
      flag++;

  }
}
