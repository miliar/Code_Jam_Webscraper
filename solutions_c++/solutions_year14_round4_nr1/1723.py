#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <vector>

using namespace std;

const int maxN=10000+13;

int a[maxN];
int v[maxN];

int N,X;

int find(int x)
{
  int l=1,r=N+1;
  while(r-l>1)
  {
    int mid=(l+r)>>1;
    if(a[mid]>x)
      r=mid;
    else
      l=mid;
  }
  while(l>=1 && v[l])
    l--;
  return l;
}

int main()
{
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);

  int ca;
  scanf("%d",&ca);
  for(int cas=1;cas<=ca;cas++)
  {
    scanf("%d%d",&N,&X);
    memset(v,0,sizeof(v));
    for(int i=1;i<=N;i++)
      scanf("%d",&a[i]);
    if(N==1)
    {
      printf("Case #%d: 1\n",cas);
      continue;
    }
    int ans(0);
    sort(a+1,a+1+N);
    for(int i=1;i<=N;i++)
    {
      if(!v[i])
      {
        if(a[i]>X-a[i])
        {
          ans++;
          continue;
        }
        int tt=find(X-a[i]);
        if(tt>i)
        {
          v[tt]=v[i]=1;
          ans++;
        }
        else
        {
          v[i]=1;
          ans++;
        }
      }
    }
    printf("Case #%d: %d\n",cas,ans);
  }
  return 0;
}






