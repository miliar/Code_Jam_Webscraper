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
int size[101010];
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("A-large.out","w",stdout);
  int T,n;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
  {
    int X;
    scanf("%d%d",&n,&X);
    for(int i=1;i<=n;i++)
      scanf("%d",size+i);
    sort(size+1,size+1+n);
    int i=1,j=n, ans=0;
    while(i<=j)
    {
      while(size[j]+size[i]>X && j>i)
      {
        ans ++;
        j--;
      }
      i++; j--;
      ans ++;
    }
    printf("Case #%d: %d\n", t, ans);
  }
  return 0;
}
