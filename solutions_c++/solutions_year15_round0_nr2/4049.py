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

const int maxN=3000+13;

int D,T;
int a[maxN];
int sp[maxN];

int main()
{
  freopen("B-small-attempt4.in","r",stdin);
  freopen("B4.out","w",stdout);

  scanf("%d",&T);
  for(int cas=1;cas<=T;cas++)
  {
    scanf("%d",&D);
    //cout<<D<<endl;
    int imax(0);
    memset(sp,0,sizeof(sp));
    for(int i=1;i<=D;i++)
    {
      scanf("%d",&a[i]);
    //  cout<<a[i]<<' ';
      sp[a[i]]++;
      upd_max(imax,a[i]);
    }
    //cout<<endl;
    int tt=0,ans=imax;
    for(int i=imax;i>=1;i--)
    {
      if(sp[i]==0) continue;
      upd_min(ans,tt+i);
      tt+=sp[i];
      if(i&1)
      {
        sp[i/2]+=sp[i];
        sp[i/2+1]+=sp[i];
        sp[i]=0;
      }
      else
      {
        sp[i/2]+=2*sp[i];
        sp[i]=0;
      }
    }
    printf("Case #%d: %d\n",cas,ans);
  }
  return 0;
}

