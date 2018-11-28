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

const int maxN=13;
const double Eps=1e-9;

int N;
double V,X;
double v[maxN],x[maxN];

bool iszero(double x)
{
  if(fabs(x)<Eps)
    return true;
  else 
    return false;
}

int main()
{
  freopen("B.in","r",stdin);
  freopen("B.out","w",stdout);

  int T;
  scanf("%d",&T);
  for(int cas=1;cas<=T;cas++)
  {
    printf("Case #%d: ",cas);
    scanf("%d%lf%lf",&N,&V,&X);
    for(int i=1;i<=N;i++)
      scanf("%lf%lf",&v[i],&x[i]);
    if(N==1)
    {
      if(!iszero(x[1]-X))
        printf("IMPOSSIBLE\n");
      else
        printf("%.8lf\n",V/v[1]);
    }
    else
    {
      if(max(x[1],x[2])<X || min(x[1],x[2])>X || ((!iszero(X-x[1]))&&iszero(x[1]-x[2])))
        printf("IMPOSSIBLE\n");
      else
      {
        if(iszero(x[1]-x[2]))
        {
          printf("%.8lf\n",V/(v[1]+v[2]));
          continue;
        }
        double ty=(V*X-V*x[1])/(x[2]-x[1]);
        double tx=V-ty;
        tx=tx/v[1];
        ty=ty/v[2];
        printf("%.8lf\n",max(tx,ty));
      }
    }
  }
  return 0;
}

