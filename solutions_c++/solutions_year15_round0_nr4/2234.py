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

int X,R,C;
int a[10][10][10];

int main()
{
  freopen("D.in","r",stdin);
  freopen("D.out","w",stdout);
  int T;
  scanf("%d",&T);
  for(int cas=1;cas<=T;cas++)
  {
    scanf("%d%d%d",&X,&R,&C);
    printf("Case #%d: ",cas);
    
    if(X==1)
      printf("GABRIEL\n");
    else if(X==2)
    {
      if((R*C)&1)
        printf("RICHARD\n");
      else
        printf("GABRIEL\n");
    }
    else if(X==3)
    {
      if((R*C)%3==0 && R*C!=3)
        printf("GABRIEL\n");
      else 
        printf("RICHARD\n");
    }
    else 
    {
      if(R*C==16 || R*C==12)
        printf("GABRIEL\n");
      else
        printf("RICHARD\n");
    }
  }

  return 0;
}

