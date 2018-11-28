#include<iostream>
#include<stdio.h>
#define MAX 1000010
using namespace std;
double f1[MAX],fsum[MAX],x1[MAX],xsum[MAX];
int main()
{
   int t,i,j,k;
   double c,f,x,m;
   scanf("%d",&t);
   k=1;   
   while(k<=t)
   {
      cin>>c>>f>>x;
      m=2;
      i=0;
      f1[0]=x/(float)m;
      fsum[0]=f1[0];
      x1[0]=c/(float)m;
      xsum[0]=x1[0];
      m=m+f;
      i=1;
      f1[1]=x/m;
      x1[1]=c/m;
      xsum[1]=xsum[0]+x1[1];
      fsum[1]=f1[1]+xsum[0];
      while(fsum[i]<fsum[i-1])
      {
          i++;
          m=m+f;
          f1[i]=x/m;
          x1[i]=c/m;
          xsum[i]=xsum[i-1]+x1[i];
          fsum[i]=f1[i]+xsum[i-1];  
                   
      } 
      printf("Case #%d: %.7f\n",k,fsum[i-1]);
      k++;
   }
   return 0; 
}
