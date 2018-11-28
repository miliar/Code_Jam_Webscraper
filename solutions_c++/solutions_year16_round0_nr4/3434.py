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

int T,K,C,S;

int main()
{
#ifndef ONLINE_JUDGE
  freopen("D-small-attempt2.in","r",stdin);
  freopen("D.out","w",stdout);
#endif
  scanf("%d",&T);
  for(int cas=1;cas<=T;cas++)
  {
    printf("case #%d: ",cas);
    scanf("%d%d%d",&K,&C,&S);
 //   cout<<K<<' '<<C<<' '<<S<<endl;
    if(K==1) 
    {
      printf("1\n");
      continue;
    }
    if(C==1)
    {
      for(int i=1;i<=K;i++)
        printf("%d ",i);
      printf("\n");
    }
    else
    {
      printf("%d ",K-1);
      for(int i=2;i<=K;i++)
        printf("%d ",K*i);
      printf("\n");
    }
  }

  return 0;
}

