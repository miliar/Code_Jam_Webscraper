#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <cmath>
#define N 10009
using namespace std;

int a[N];
int n;
int t;

int main()
{

    //freopen("test.in","r",stdin);
    //freopen("test.out","w",stdout);

   while(~scanf("%d",&t))
   {
       int ca=1;
       while(t--)
       {
           scanf("%d",&n);
           int mmax=0;
           int num;
           int ans=1000000009;
           int pp;

           for(int i=0;i<n;i++)
           {
               scanf("%d",&a[i]);
               mmax=max(mmax,a[i]);
           }

           for(int i=1;i<=mmax;i++)
           {
               num=0;
               for(int j=0;j<n;j++)
               {
                   pp=a[j]/i+(a[j]%i==0?0:1)-1;
                   num+=pp;
               }
               ans=min(ans,num+i);
           }
           printf("Case #%d: %d\n",ca++,ans);

       }
   }
    return 0;
}
