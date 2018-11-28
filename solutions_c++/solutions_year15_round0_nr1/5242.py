/*
 *
 * Author : fcbruce <fcbruce8964@gmail.com>
 *
 * Time : Sat 11 Apr 2015 02:53:39 PM CST
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

int main()
{
#ifdef FCBRUCE
  freopen("/home/fcbruce/code/t","r",stdin);
  freopen("A.out","w",stdout);
#endif // FCBRUCE

  int T_T,__=0;
  scanf("%d",&T_T);

  while (T_T--)
  {
    int n;
    scanf("%d",&n);

    int total=0;
    int invite=0;

    for (int i=0;i<=n;i++)
    {
      int k;
      scanf("%1d",&k);
      if (total<i)
      {
        invite+=i-total;
        total=i;
      }

      total+=k;
    }

    printf("Case #%d: %d\n",++__,invite);
  }




  return 0;
}
