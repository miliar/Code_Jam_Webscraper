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
int worst, total;
int m,n, pre[10][10];
string S[10];
int where[10];
int cnt[10];
void init()
{
  cin>>m>>n;
  for(int i=1;i<=m;i++)
    cin>>S[i];
  worst=0;
  total=0;
  for(int i=1;i<m;i++)
    for(int j=i+1;j<=m;j++)
    {
      int l=min(S[i].size(),S[j].size());
      bool xxx=false;
      for(int k=0; k<l; k++)
        if (S[i][k] != S[j][k])
        {
          xxx=true;
          pre[i][j]=pre[j][i]=k;
          break;
        }
      if (!xxx)
        pre[i][j]=pre[j][i]=l;
    }
}
bool ok()
{
  for(int i=1;i<=n;i++)
    cnt[i]=0;
  for(int i=1;i<=m;i++)
    cnt[where[i]]++;
  for(int i=1;i<=n;i++)
    if(cnt[i]==0)
      return false;
  return true;
}
void dfs(int now)
{
  if (now>m)
  {
    if (ok())
    {
      int tmp=0;
      for(int i=1;i<=m;i++)
      {
        tmp+=S[i].size();
        int k=0;
        for(int j=1;j<i;j++)
          if (where[j]==where[i])
            if (k==0 || pre[i][j]>pre[i][k])
              k = j;
        if (k>0)
          tmp -= pre[i][k];
      }
      tmp += n;
      if (tmp>worst)
      {
        worst=tmp;
        total=0;
      }
      if (tmp==worst)
        total++;
    }
    return;
  }
  for(int s=1;s<=n;s++)
  {
    where[now]=s;
    dfs(now+1);
  }
}
void work()
{
  dfs(1);
  printf("%d %d\n", worst, total);
}
int main()
{
  freopen("D-small-attempt1.in","r",stdin);
  freopen("D-small-attempt1.out","w",stdout);
  int T;
  cin>>T;
  for(int t=1;t<=T;t++)
  {
    init();
    printf("Case #%d: ",t);
    work();
  }
  return 0;
}
