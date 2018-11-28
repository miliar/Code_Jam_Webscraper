             /*
     shubham_1286(shubham verma)
                                   */
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<vector>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<list>
#include<deque>
#include<bitset>
#include<limits.h>
#include<sstream>
#define max(x,y) x>y?x:y
#define min(x,y) x<y?x:y
#define sd(a)  scanf("%d",&a);
#define slld(a)  scanf("%lld",&a);
#define sllu(a)  scanf("%llu",&a);
#define pd(a)  printf("%d\n",a);
#define plld(a)  printf("%lld\n",a);
#define pllu(a)  printf("%llu\n",a);
#define inf INT_MAX
#define low INT_MIN
#define mod 1000000009
#define ull unsigned long long
#define ll long long
using namespace std;
int main()
{
// freopen("c:\\users\\verma\\desktop\\large.txt","r",stdin);
  //freopen("c:\\users\\verma\\desktop\\out6.txt","w",stdout);
 int t,testcase=1;
 sd(t);
 while(testcase<=t)
 {
        
    ll p,q,ans=0;
    scanf("%lld/%lld",&p,&q);
    ll x=__gcd(p,q);
    p=p/x;
    q=q/x;
    ll gg=q&(q-1);
    if(gg!=0)
    {
        printf("Case #%d: impossible\n",testcase);
    }
    else
    {
        
      ll ff=log2(p);
      ll xx=log2(q);
      if((q-1)==p)
         ans=1;
         else
      ans+=(xx-ff);
    
    if(p==1&& gg==0 )
    printf("Case #%d: %d\n",testcase,xx);
    else if(p!=1 &&gg==0) 
     printf("Case #%d: %d\n",testcase,ans);
   }
     testcase++;
}  
}
