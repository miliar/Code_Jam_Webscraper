#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<set>
#include<vector>
#include<cstring>
#include<string>
#define s(a) scanf("%lld",&a)
#define p(a) printf("%lld",a)
#define MAX(A,B) A>B?A:B
#define MIN(A,B) A<B?A:B

using namespace std;

typedef long long ll;

ll GCD(ll A, ll B)  {  if(B==0) return A;  return GCD(B,A%B); }

int main()
{
   freopen("//home//vivek//Desktop//input.txt","r",stdin);
   freopen("//home//vivek//Desktop//output.txt","w",stdout);
   ll T,tt,cnt,i,j,A,B,K;
   cin>>T;
   for(tt=1;tt<=T;tt++)
   {
      cin>>A>>B>>K;
      cnt=0;
      for(i=0;i<A;i++)
      {
         for(j=0;j<B;j++)
         {
            if((i&j) < K) cnt++;
         }
      }
      cout<<"Case #"<<tt<<": "<<cnt<<endl;
   }

   return 0;
}

