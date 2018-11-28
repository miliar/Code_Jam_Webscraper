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

int tc,cs=1,n,p,lmt,cnt,bin[18];
ll base[12][17],check[13],num,sqt;
bool fl;

void fun()
{
   for(int i=2;i<=10;i++)
   {
      base[i][0]=1ll;
      for(int j=1;j<=16;j++)
      {
         base[i][j]=(ll)(base[i][j-1]*i);

         //cout<<base[i][j]<<"  ";
      }
   }
}

int main()
{
   fun();

   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   s1(tc);
   int c=0;
   while(tc--)
   {
      s2(n,p);
      lmt=(1<<(n-1));
      c=0;
      printf("Case #1:\n");

      for(int i=1;i<lmt;i+=2)
      {
         cnt=0;
         bin[n-1]=1;

         for(int j=2;j<=10;j++)
         {
            num=base[j][n-1];
            for(int k=0;k<(n-1);k++)
            {
              if(i & (1<<k))
              {
                  num+=base[j][k];
                  bin[k]=1;
              }
              else bin[k]=0;
            }
//            cout<<num<<"----->\n";
            sqt=(ll)sqrt(num);

            //cout<<sqt<<endl;
            for(ll k=2;k<=sqt;k++)
            {
               fl=0;
               if(num%k==0)
               {
                  for(int l=0;l<cnt;l++)
                  {
                     if(check[l]==k)
                     {
                        fl=1;
                        break;
                     }
                  }
                  if(!fl)
                  {
                     check[cnt]=k;
                     cnt++;
                     break;
                  }
               }
            }
            if(cnt==9)break;
         }

         if(cnt==9)
         {
            for(int j=n-1;j>=0;j--)printf("%d",bin[j]);
            for(int j=0;j<cnt;j++)printf(" %lld",check[j]);
            c++;
            NL;
         }

         if(c==p)break;

      }

   }
   return 0;
}



