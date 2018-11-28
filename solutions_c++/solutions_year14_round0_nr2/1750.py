#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<iomanip>
using namespace std;    //  c=30 ,  f=2 , x=100       ,v=2
int main()
{
 int g,t;
 double c,f,x,v,one,two,a,ans;
 cin>>t;
 for(g=0;g<t;g++)
 {
  cin>>c>>f>>x;
  v=2;

  one=x/v;
  two=(c/v)+(x/(v+f));
  a=c/v;
  if(one<two)
  {      printf("Case #%d: %.7f\n",g+1,x/v);
  continue;  }

  else
  {
   while(1)
   {
     v=v+f;
     ans= a+(c/v)+(x/(v+f));
     a=a+(c/v);
                  
     if(ans<two)   two=ans;
     else  {   printf("Case #%d: %.7f\n",g+1,two);
 break;
           }
   }
  }

 }
 return 0;
}
   
     
     
  