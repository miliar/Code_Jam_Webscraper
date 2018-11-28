/*
   nitesh kumar (codeshaker)
*/

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <vector>
#include <string>
#include <bitset>
#include <climits>
#include <complex>
typedef long long LL;
using namespace std;
int main(void)
{
  int i,j,k,tc,ans1=0,ans2=0;
  scanf("%d",&tc);
  int t;
  for(t=1;t<=tc;t++)
  {
    ans1=ans2=0;
     int n;
     scanf("%d",&n);
     double v1[1005],v2[1005];
     for(i=0;i<n;i++)
     {
       scanf("%lf",&v1[i]);
     }
      for(i=0;i<n;i++)
     {
       scanf("%lf",&v2[i]);
     }
     sort(v1,v1+n);
     sort(v2,v2+n);
     i=0,j=0;
      for(i=0;i<n;i++)
      {
       if(v1[i]>v2[j])
        {
           j++;
           ans1++;
        }
      }

     ans2=n;
     i=n-1,j=n-1;
     for(i=n-1;i>=0;i--)
       {
       if(v1[i]<v2[j])
        {
           j--;
           ans2--;
        }
    }

     printf("Case #%d: ",t);
     printf("%d %d\n",ans1,ans2);
  }
  return 0;
}
