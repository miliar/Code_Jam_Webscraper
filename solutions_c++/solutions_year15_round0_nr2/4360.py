/*
 *
 * Author : fcbruce <fcbruce8964@gmail.com>
 *
 * Time : Sat 11 Apr 2015 03:17:24 PM CST
 *
 */
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <algorithm>
#include <ctime>
#include <cctype>
#include <cmath>
#include <string>
#include <cstring>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <set>
#define sqr(x) ((x)*(x))
#define LL long long
#define itn int
#define INF 0x3f3f3f3f
#define PI 3.1415926535897932384626
#define eps 1e-10

#ifdef _WIN32
  #define lld "%I64d"
#else
  #define lld "%lld"
#endif

#define maxm 
#define maxn 

using namespace std;

int p[123333];

int main()
{
#ifdef FCBRUCE
  freopen("/home/fcbruce/code/t","r",stdin);
  freopen("B.out","w",stdout);
#endif // FCBRUCE

  int T_T,__=0;
  scanf("%d",&T_T);

  while (T_T--)
  {

    int d;
    scanf("%d",&d);

    for (int i=0;i<d;i++) 
    {
      scanf("%d",p+i);
    }


    sort(p,p+d);
    int res=p[d-1];
    int c=res;

    for (int i=1;i<=c;i++)
    {
      for (int j=i;j>=(int)ceil(i*1.0/d);j--)
      {
        int cut=i-j;
        int m=(int)ceil(p[d-1]*1.0/(j+1));
        for (int k=d-2;k>=0;k--)
        {
          if (cut==0)
          {
            m=max(m,p[k]);
            break;
          }
          else if (cut>=j)
          {
            cut-=j;
            m=max(m,(int)ceil(p[k]*1.0/(j+1)));
          }
          else
          {
            m=max(m,(int)ceil(p[k]*1.0/(cut+1)));
            cut=0;

          }
        }
        res=min(res,m+i);
      }
    }

    printf("Case #%d: %d\n",++__,res);

    
  }



  return 0;
}
