// b@ver
#include<cstdio>
#include<iostream>
#include<algorithm>
#include <cmath>
#include <vector>
#include<cstring>
#include<cstdlib>
using namespace std;
int main()
{
   freopen("B-large.in","r",stdin);
   int t,var;
   scanf("%d",&t);
   var=t;
   while(t--)
   {
      double c,f,x,ans=0,comp=0,temp=0,tm,temp1=0;
      cin>>c>>f>>x;
      tm=2;
      if(x<=c)
      {
         ans=x/2;
         printf("Case #%d: %.7lf\n",var-t,ans);
      }
      else
      {
         comp=x/2;
         tm+=f;
         temp1+=c/2;
         temp=temp1+(x/tm);
         if(temp>=comp)
         {
            printf("Case #%d: %.7lf\n",var-t,comp);
         }
         else
         {
            //comp=temp;
            while(temp<comp)
            {
               comp=temp;
               temp1+=(c/tm);
               tm+=f;
               temp=temp1+(x/tm);
            }
            printf("Case #%d: %.7lf\n",var-t,comp);
         }
      }
   }
   return 0;
}
