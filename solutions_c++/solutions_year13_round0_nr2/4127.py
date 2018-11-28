 #include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <limits>
#include <cctype>

using namespace std;

int arr[150][150],n,m;
int row[150],col[150];

bool check()
{
    int t[150][160];
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
         {
             t[i][j]=min(row[i],col[j]);
             if(t[i][j]!=arr[i][j])
                return 0;
         }
         return 1;
}
int main()
{
  freopen("2.in","r",stdin);
   freopen("3.out","w",stdout);
  int tc;
  scanf("%d ",&tc);
  for(int ic=1;ic<=tc;ic++)
  {
      scanf("%d %d ",&n,&m);
      for(int i=0;i<n;i++)
      {
          row[i]=0;
          for(int j=0;j<m;j++)
          {
              scanf("%d ",&arr[i][j]);
              row[i]=max(row[i],arr[i][j]);
          }
      }

      for(int i=0;i<m;i++)
      {
          col[i]=0;
          for(int j=0;j<n;j++)
          {
              col[i]=max(col[i],arr[j][i]);
          }
      }
      printf("Case #%d: ",ic);
      if(check())
        printf("YES\n");
      else
        printf("NO\n");

  }
}

