#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <utility>
#include <string>
#include <set>
#include <map>

using namespace std;

#define loop(i,x,y) for(i=x;i<y;i++)

#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define sllu(x) scanf("%llu",&x)
#define sstr(x) scanf("%s",x)

#define pd(x) printf("%d",x)
#define plld(x) printf("%lld",x)
#define pllu(x) printf("%llu",x)
#define pstr(x) printf("%s",x)
#define pnl printf("\n")
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)

typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long int lld;
typedef unsigned long long int llu;

int main()
{
   int i,t,sum,tot,n,j;
   string ar;
   sd(t);
   loop(j,0,t)
   {
      sd(n);
      cin>>ar;
      n++;
      sum=0;
      tot=0;
      loop(i,0,n)
      {
         if((ar[i]-'0')>0)
         {
            if(tot<i)
            {
               sum+=(i-tot);
               tot+=(i-tot);
            }
            tot+=ar[i]-'0';
            
         }
      }
      printf("Case #%d: %d\n",j+1,sum);
   }
   return 0;
}