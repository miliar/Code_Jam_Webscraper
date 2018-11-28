#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<stdlib.h>
#include<algorithm>
#include<limits.h>
using namespace std;
long long int gcd(long long int a,long long int b)
{
	if (b==0)
		return a;
	else
		return gcd(b,a%b);
}
int main()
{
    long long int T,t,i,cu,n,k,a[1000],b[1000],c[1000],lcm,hcf,cy;
    freopen("B-small-attempt0 (1) - Copy.in","r",stdin); freopen("gcjbsmallout.txt","w",stdout);
    scanf("%lld",&T);
    for(t=1;t<=T;t++)
    {
                     scanf("%lld %lld",&n,&k);
                     for(i=1;i<=n;i++)
                     {
                                      scanf("%lld",&a[i]);
                     }
                     lcm=a[1];
                     for(i=2;i<=n;i++)
                     {
                                      hcf=gcd(a[i],lcm);
                                      lcm=(lcm*a[i])/hcf;
                     }
                     cy=0;
                     for(i=1;i<=n;i++)
                     {
                                     cy=cy+lcm/a[i];
                     }
                     k=k%cy;
                     if(k==0)
                     k=cy;
                     for(i=1;i<=n;i++)
                     {
                                      b[i]=0;
                     }
                     cu=1;
                     while(cu<=k)
                     {
                             for(i=1;i<=n;i++)
                             {
                                              if(b[i]==0)
                                              {
                                                         b[i]=a[i];
                                                         c[i]=cu;
                                                         cu++;
                                              }
                             }
                             for(i=1;i<=n;i++)
                             {
                                              b[i]--;
                             }
                     }
                     for(i=1;i<=n;i++)
                     {
                                      if(c[i]==k)
                                      break;
                     }
                     printf("Case #%lld: %lld\n",t,i);
    }
    return 0;
}
