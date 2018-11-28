#include<stdio.h>
#include<iostream>
#include<math.h>
#include<string.h>
#include<algorithm>
typedef long long int ll;
using namespace std;
int main()
{
   FILE *op=fopen("output.in","w");
   FILE *ip=fopen("B-large.in","rt");
   ll a[100000];
ll t,t1,n,i,max,p,j,p1,max1;
fscanf(ip,"%lld",&t);
for(t1=1;t1<=t;t1++)
{
    max=0;
    fscanf(ip,"%lld",&n);
    for(i=1;i<=n;i++)
    {
      fscanf(ip,"%lld",&a[i]);
      if(a[i]>=max)
      {
           max=a[i];
      }
    }
       p=max;
    for(i=1;i<=max;i++)
    {
        max1=0;
        p1=0;
        for(j=1;j<=n;j++)
        {
            if(a[j]>i)
            {
                if(a[j]%i==0)
                {
                    p1=p1+(a[j]/i)-1;
                }
                else
                  p1=p1+(a[j]/i);

                  if(i>=max1)
                    max1=i;
            }
            else
            {
                if(a[j]>=max1)
            max1=a[j];
            }
        }
        p1=p1+max1;
        if(p1<p)
            p=p1;
    }
      fprintf(op,"Case #%lld: %lld\n",t1,p);
}
return 0;
}
