#include <iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

double a[1005],b[1005];
int main()
{
   freopen("D-large.in","r",stdin);
   freopen("output.in","w",stdout);
   int test,n,i,i1,j1,c1,tt,c2;
   scanf("%d",&test);
   for(tt=1;tt<=test;tt++)
   {
       scanf("%d",&n);
       for(i=0;i<n;i++)
       scanf("%lf",&a[i]);
       for(i=0;i<n;i++)
       scanf("%lf",&b[i]);
       sort(a,a+n);
       sort(b,b+n);
       i1=0;j1=n-1;
       c1=0;
       for(i=0;i<n;i++)
       {
           if(a[i]<b[i1])
           j1--;
           else if(a[i]>b[i1])
           {
               i1++;
               c1++;
           }
       }
       j1=n-1;c2=0;
       for(i=n-1;i>=0;i--)
       {
           if(a[i]>b[j1])
           c2++;
           else if(a[i]<b[j1])
           j1--;
       }
       printf("Case #%d: ",tt);
       printf("%d %d\n",c1,c2);
   }
   return 0;
}
