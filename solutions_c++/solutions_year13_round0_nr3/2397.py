                /* Original Author: Akash Sinha(sinaka)
                       Problem Code:
                       Language: c++
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
//#include<conio.h>

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
int main()
{
    freopen("C:\\Users\\tantrik\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\tantrik\\Desktop\\output.txt","w",stdout);
    ULL i,j,k,c=0,t,x,y,tc;
    ULL arr[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,
              102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,
              10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,
              1020304030201,1022325232201,1024348434201,
              1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,
              4004009004004};
    scanf("%llu",&t);
    for(tc=1;tc<=t;tc++)
    {
       scanf("%llu%llu",&x,&y);
       c=0;
       for(i=0;i<39;i++)
       if((arr[i]>=x)&&(arr[i]<=y))
       c++;
       printf("Case #%llu: %llu\n",tc,c);
    }
    return 0;
}
