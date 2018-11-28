/*
|-------------------------|
| Pronab Malaker(prnb22)  |
|-------------------------|
*/
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <iostream>
#include <fstream>
#include <numeric>
#include <string>
#include <vector>
#include <cstring>
#include <map>
#include <iterator>
#include <deque>
#include <climits>
#include <complex>
#include <bits/stdc++.h>

using namespace std;

/*......define........*/
#define pi          2.0*acos(0.0)
#define ull         unsigned long long
#define ll          long long int
#define pb(a)       push_back(a)
#define pf(a)       push_front(a)
#define ppb         pop_back()
#define ppf         pop_front()
#define UB          upper_bound
#define LB          lower_bound
#define SZ()        size()

#define s1(a)       scanf("%d",&a)
#define s2(a,b)     scanf("%d%d",&a,&b)
#define s3(a,b,c)   scanf("%d%d%d",&a,&b,&c)
#define sl1(a)      scanf("%lld",&a)
#define sl2(a,b)    scanf("%lld%lld",&a,&b)
#define sl3(a,b,c)  scanf("%lld%lld%lld",&a,&b,&c)
#define sul1(a)     scanf("%llu",&a)
#define sul2(a,b)   scanf("%llu%llu",&a,&b)
#define sul3(a,b,c) scanf("%llu%llu%llu",&a,&b,&c)

#define f(i,a,b)    for(int i=a;i<=b;i++)
#define rev(i,a,b)  for(int i=b;i>=a;i--)
#define fi          first
#define se          second
#define MP          make_pair
#define mem(a,v)    memset(a,v,sizeof a)
#define OnBit(a)    __builtin_popcountll(a)

#define PC(a)       printf("Case %d: ",a)
#define P1(a)       printf("%d",a)
#define P2(a,b)     printf("%d %d",a,b)
#define P3(a,b,c)   printf("%d %d %d",a,b,c)

#define PL1(a)      printf("%lld",a)
#define PL2(a,b)    printf("%lld %lld",a,b)
#define PL3(a,b,c)  printf("%lld %lld %lld",a,b,c)

#define NL          printf("\n")


template <typename T> T BigMod (T b,T p,T m)
{
    if (p == 0) return 1;
    if (p%2 == 0)
    {
        T s = BigMod(b,p/2,m);
        return ((s%m)*(s%m))%m;
    }
    return ((b%m)*(BigMod(b,p-1,m)%m))%m;
}
template <typename T> T ModInv (T b,T m)
{
    return BigMod(b,m-2,m);
}
template <typename T> T lcm(T a,T b)
{
    if(a<0)return lcm(-a,b);
    if(b<0)return lcm(a,-b);
    return a*(b/__gcd(a,b));
}

double DEG(double x)
{
    return (180.0*x)/(pi);
}
double RAD(double x)
{
    return (x*(double)pi)/(180.0);
}

#define MX  30000000
#define MOD 1000000007
#define INF (1<<30)-1
#define eps 1e-9

int tc,cs=1;
char s[110];
int r1,r2,l,b1[110],b2[110];



int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   s1(tc);
   while(tc--)
   {
      scanf("\n%s",&s);
      l=strlen(s);
      //printf("%s\n",s);
      //cout<<s<<endl;
      for(int i=0;i<l;i++)
      {
         if(s[i]=='+')b1[i]=1,b2[i]=1;
         else b1[i]=0,b2[i]=0;

         //cout<<b1[i]<<" "<<b2[i]<<endl;
      }
      r1=0;
      r2=0;

      for(int i=l-1;i>=0;i--)
      {
         if(b1[i]==0)
         {
           r1++;
           for(int j=0;j<=i;j++)b1[j]^=1;
         }
//         for(int j=0;j<l;j++)cout<<b1[j];
//         cout<<endl;
      }
//      cout<<"-----\n";
      for(int i=l-1;i>=0;i--)
      {
         if(b2[i]==1)
         {
           r2++;
           for(int j=0;j<=i;j++)b2[j]^=1;
         }
//         for(int j=0;j<l;j++)cout<<b2[j];
//         cout<<endl;
      }
      r2++;
//      cout<<r1<<" "<<r2<<endl;
      printf("Case #%d: %d\n",cs++,min(r1,r2));
   }
   return 0;
}


