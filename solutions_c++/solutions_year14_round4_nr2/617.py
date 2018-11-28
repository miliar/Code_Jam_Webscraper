#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <algorithm>
#include <set>
#include <new>
#define see(x) cerr<<#x<<" = " << (x) << endl
using namespace std;
int num[1010],pre[1010];
int main()
{
  freopen("B-large.in","r",stdin);
  freopen("B-large.out","w",stdout);
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
  {
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
      scanf("%d",num+i);
    memset(pre,0,sizeof(pre));
    int ans=0;
    for(int i=1;i<=n;i++)
    {
      int M=0;
      for(int j=1;j<=n;j++)
        if (pre[j] == pre[j-1])
        {
          if (M==0 || num[j]<num[M])
            M=j;
        }
      ans += min(M-pre[M]-1, n+1-i-(M-pre[M]));
      for(int j=M; j<=n; j++)
        pre[j] ++;
    }
    printf("case #%d: %d\n", t, ans);
  }
  return 0;
}
