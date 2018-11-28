#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
#include<ctype.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<deque>
#include<queue>
#include<set>
#include<vector>
#include<stack>
#include<map>
#include<list>
#include<functional>


using namespace std;

#define loop(i,n) for(i=0;i<n;i++)
#define loop1(i,n) for(i=1;i<=n;i++)
#define loop2(i,n,k) for(i=n;i<k;i++)
#define loop3(i,n,k) for(i=n;i<=k;i++)
#define loopr(i,n,k) for(i=n;i>=k;i--)
#define si(n) scanf("%d",&n)
#define sli(n) scanf("%ld",&n)
#define slli(n) scanf("%lld",&n)
#define fast(n) n=input()
#define sc(n) scanf("%c",&n)
#define ss(n) scanf("%s",n)
#define sf(n) scanf("%f",&n)
#define slf(n) scanf("%lf",&n)
#define sllf(n) scanf("%llf",&n)
#define pin(n) printf("%d\n",n)
#define pfn(n) printf("%f\n",n)
#define psn(n) printf("%s\n",n)
#define pcn(n) printf("%c\n",n)
#define pcw(n) printf("%c ",n)
#define ps(n) printf("%s",n)
#define pc(n) printf("%c",n)
#define piw(n) printf("%d ",n)
#define pfw(n) printf("%f ",n)
#define psw(n) printf("%s ",n)
#define plin(n) printf("%ld\n",n)
#define pdn(n) printf("%lf\n",n)
#define pliw(n) printf("%ld ",n)
#define pdw(n) printf("%lf ",n)
#define pllin(n) printf("%lld\n",n)
#define pldn(n) printf("%llf\n",n)
#define plliw(n) printf("%lld ",n)
#define pldw(n) printf("%llf ",n)
#define pw printf(" ")
#define pn printf("\n")


#define MAX 1000000


 typedef long long int LL;
 typedef long int L;
 typedef long double LD;
 typedef unsigned long long int ULL;

 inline LL input() {
 char c = getchar();
 while(c<'0' || c>'9') c = getchar();
LL ret = 0;
 while(c>='0' && c<='9') {
 ret = 10 * ret + c - 48;
 c = getchar();
 }
 return ret;
 }

int main()
{
   LL i,j,k=0,l,n,t;
   double p,q,r,s,a[1000],b[1000];
  slli(t);
  while(t--)
  {
      k++;
      slli(n);
      loop(i,n)
      {
          slf(a[i]);
          
      }
      loop(i,n)
      {
      	slf(b[i]);
      }
      sort(a,a+n);
      sort(b,b+n);
      i=0;
      j=0;
      LL count=0,ans1=0,ans2=0;
      while(j<n)
      {
          if(b[j]>a[i])
          {
              count++;
              i++;
              j++;
          }
          else
            j++;
      }
      ans2=n-count;
      count=0;
      i=0;
      j=0;
      while(i<n)
      {
          if(b[j]<a[i])
          {
              count++;
              i++;
              j++;
          }
          else
            i++;
      }
      ans1=count;
      printf("Case #%lld: %lld %lld\n",k,ans1,ans2);

  }
return 0;
}
