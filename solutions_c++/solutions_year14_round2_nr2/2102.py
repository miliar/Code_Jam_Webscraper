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
// freopen("c:\\users\\verma\\desktop\\aa.txt","r",stdin);
  //freopen("c:\\users\\verma\\desktop\\out.txt","w",stdout);
  int t,test=1;
  sd(t);
  while(test<=t)
  {
        int a,b,k,coun=0;
        
        sd(a);sd(b);sd(k);
        
        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                if((i&j)<k)
                coun++;
            }
        }
        printf("Case #%d: %d\n",test,coun);
       test++;
    }
 // system("pause");
 }
