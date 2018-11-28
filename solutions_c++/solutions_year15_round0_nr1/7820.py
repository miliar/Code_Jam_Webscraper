#include<bits/stdc++.h>
using namespace std;
#define M 1000003
typedef vector<long long> vi; 
typedef vector<vi> vvi; 
typedef pair<long long,long long> ii; 
typedef long long LL;
typedef unsigned long long ULL;
long long expo(LL a,LL b,LL m){
   LL result = 1;
   while (b){
      if (b&1){
         result=  (result*a)%m;
      }
      b= (b >>1)%m ;
      a= (a*a)%m;
   }
 
  return result;
}

ULL msb(ULL n)
{
   for (long long i=63; i>=0; i--)
   {
      /* code */
      if((n&(1ll<<i))!=0)
         return 1ll<<i;
   }
   return 0;
}
LL fact(LL x)
{
   LL ans=1;
   if(x<=0)
      return 1;
   while(x)
   {
      ans=(ans*x)%M;
      x--;
   }
   return ans;
}
LL comb(LL n,LL r)
{
   if(r==n||r==0)
      return 1;
   else if(r>n)
      return 0;
   if(r>n-r)
      r=n-r;

   LL ans=1,x=n;
   while(x>=n-r+1)
   {
      ans=(ans*x)%M;
      x--;
   }
   return (ans*expo((fact(r)%M),M-2,M))%M;
}
int main()
{
   int t;
   char s[10000];
   cin>>t;
   for (int i = 0; i <t; ++i)
   {
      /* code */
      int count=0,ans=0,smax;
      cin>>smax>>s;
      for (int j = 0; j < strlen(s); ++j)
      {
         /* code */
         
         if(count>=j)
         {
            count+=s[j]-'0';


         }
         else
         {
            ans+= j-count;
            count=j+s[j]-'0';

         }
      }
      printf("Case #%d: %d\n",i+1,ans);

   }
 
}






