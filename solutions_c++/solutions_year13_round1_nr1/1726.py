                    /* Original Author: sinaka(Akash Sinha)
                       Language: C++ 4.3.2
                    */
using namespace std;
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <bitset>

//DEFINITIONS

#define LL  long long int
#define ULL  unsigned long long int
#define DB double
#define LDB long double
#define PB push_back
#define MP make_pair
#define SL(a) scanf("%lld",&a)
#define S(a) scanf("%d",&a)
#define SC(a) scanf("%c",&ch)
#define SD(a) scanf("%lf",&a)
#define PL(a) printf("%lld",a)
#define P(a) printf("%d",a)
#define PC(a) printf("%c",a)
#define PD(a) printf("%lf",a)
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define NL printf("\n")
#define W(t) while(t--)
#define FOR(i,lo,hi) for(i=lo;i<hi;i++)
#define gc getchar_unlocked
#define MOD 1000000007

// main function
int main()
{
   freopen("C:\\Users\\suyash\\Desktop\\input.txt","r",stdin);
   freopen("C:\\Users\\suyash\\Desktop\\output.txt","w",stdout);
   int t,a,i,k,j,r,tc,x,y,z;
   scanf("%d",&tc);
   for(a=1;a<=tc;a++)
   {
      scanf("%d%d",&r,&t);
      x=0;y=0;
      //cout<<x<<endl;
      for(i=r;;i+=2)
      {
         if(y>t)
         break;
         //cout<<x<<endl;
         z=(i+1)*(i+1);
         z-=i*i;
         if(z+y<=t)
         {
            y+=z;
            x++;
         }
         else if(z+y>t)
         break;
      }
      printf("Case #%d: %d\n",a,x);
   }
   return 0;
}
