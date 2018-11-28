#include <algorithm>
#include <iostream>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <map>

using namespace std;

template <typename T>
inline void upd_max(T &dest,const T& src){if(dest<src)dest=src;return ;}
template <typename T>
inline void upd_min(T &dest,const T& src){if(dest>src)dest=src;return ;}

int v[100];

int cal(int n)
{
  memset(v,0,sizeof(v));
  for(int i=1;i<=100;i++)
  {
    int tt=n*i;
    while(tt)
    {
      v[tt%10]=1;
      tt/=10;
    }
    bool ok=true;
    for(int j=0;j<=9;j++)
      ok&=v[j];
    if(ok) return i;
  }
  return -1;
}

int N,tt;

int main()
{
#ifndef ONLINE_JUDGE
  freopen("A.out","w",stdout);
  freopen("A-large.in","r",stdin);
#endif
  
  scanf("%d",&N);
  for(int i=1;i<=N;i++)
  {
    printf("Case #%d: ",i);
    scanf("%d",&tt);
    int tn=cal(tt);
    if(tn==-1) 
      printf("INSOMNIA\n");
    else
      printf("%d\n",tn*tt);
  }

  return 0;
}

