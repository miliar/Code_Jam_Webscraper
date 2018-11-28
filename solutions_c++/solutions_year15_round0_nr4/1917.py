#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<queue>
#include<list>
#include<map>
using namespace std;
#define gc getchar//_unlocked
#define pc(x) putchar(x)//_unlocked(x)
//#define pc(x) putchar_unlocked(x)

 int read_int() {
      char c = gc();
      while(c<'0' || c>'9') c = gc();
      int ret = 0;
      while(c>='0' && c<='9') {
        ret = 10 * ret + c - 48;
        c = gc();
      }
      return ret;
}

long long int lread_int() {
      char c = gc();
      while(c<'0' || c>'9') c = gc();
      long long int ret = 0;
      while(c>='0' && c<='9') {
        ret = 10 * ret + c - 48;
        c = gc();
      }
      return ret;
}
inline void scanint(int &x)
{
   register int c = gc();
   x = 0;
   int neg = 0;
   for(;((c<48 || c>57) && c != '-');c = gc());
   if(c=='-') {neg=1;c=gc();}
   for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
   if(neg) x=-x;
}
inline void scanllint(long long int &x)
{
   long long int c = gc();
   x = 0;
   long long int neg = 0;
   for(;((c<48 || c>57) && c != '-');c = gc());
   if(c=='-') {neg=1;c=gc();}
   for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
   if(neg) x=-x;
}
long long int gcd(long long int a,long long int b){
    if ( a==0 ) return b;
  return gcd ( b%a, a );
}

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        int x,r,c,i,j,ans;
        scanf("%d",&x);
        scanf("%d",&r);
        scanf("%d",&c);
        if(x==1)
        {
            ans=1;
        }
        else if(x==2)
        {
            if(((r%2)!=0)&&((c%2)!=0))
                ans=0;
            else
                ans=1;
        }
        else if(x==3)
        {
            if((r==2&&c==3)||(r==3&&c==2)||(r==3&&c==3)||(r==3&&c==4)||(r==4&&c==3))
                ans=1;
            else
                ans=0;
        }
        else if(x==4)
        {
            if((r==4&&c==4)||(r==3&&c==4)||(r==4&&c==3))
                ans=1;
            else
                ans=0;
        }
        if(ans==0)
        {
            printf("Case #%d: RICHARD\n",k);
        }
        else
        {
            printf("Case #%d: GABRIEL\n",k);
        }
    }
    return 0;
}
