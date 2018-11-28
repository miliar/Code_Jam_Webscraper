#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{ int t,ch=0;
  double f,x,cps,cookies=0,c,time;
  cin>>t;
  while(t--)
   { ++ch;
     cps=2;
     scanf("%lf%lf%lf",&c,&f,&x);
     time=0;
     while(1)
       { if ( (x/cps) <= ( (c/cps) + (x/(cps+f)) ) )break; 
       	 time+=(c/cps);
       	 cps+=f;
       }
     time+=(x/cps); 
   	 printf("Case #%d: %.7f\n",ch,time);
   }
  return 0;	
}
