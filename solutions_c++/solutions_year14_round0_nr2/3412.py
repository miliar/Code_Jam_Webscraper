#include <iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

int main()
{
    int t;
    scanf("%d",&t);
    FILE *ptr;
    ptr=fopen("file.txt","w");

    for(int i=1;i<=t;i++)
    {
      double c,f,x,rate=2.0;
      double time=0.0;
      double cookies=0.0;
      scanf("%lf%lf%lf",&c,&f,&x);

      if(c>=x)
      {
          fprintf(ptr,"Case #%d: %.7lf\n",i,(x-cookies)/rate);
          continue;
      }

      while(cookies<x)
      {
          time+=(c)/rate;
          cookies=c;

          if((time+(x-cookies)/rate)>(time+(x/(rate+f))))
          {
              cookies=0;
              rate+=f;
          }
          else
          {
           time+=(x-cookies)/rate;
           break;
          }
      }
      fprintf(ptr,"Case #%d: %.7lf\n",i,time);
    }
    fclose(ptr);
    return 0;
}
