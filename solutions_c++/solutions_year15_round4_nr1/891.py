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

const int maxN=100+13;
const int dx[5]={0,0,1,-1};
const int dy[5]={1,-1,0,0};

char c[maxN][maxN];
int R,C,T;

int main()
{
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);

  scanf("%d",&T);
  for(int cas=1;cas<=T;cas++)
  {
    printf("Case #%d: ",cas);
    scanf("%d%d",&R,&C);
    for(int i=1;i<=R;i++) 
      scanf("%s",&c[i][1]);
    int ans=0;
    bool pos=true;
    for(int i=1;i<=R;i++)
    {
      for(int j=1;j<=C;j++)
      {
        if(c[i][j]=='.')continue;
        int dd=-1;
        if(c[i][j]=='^')dd=3;
        if(c[i][j]=='v')dd=2;
        if(c[i][j]=='<')dd=1;
        if(c[i][j]=='>')dd=0;
        bool ok=false;
        for(int k=1;;k++)
        {
          int tx,ty;
          tx=i+k*dx[dd];
          ty=j+k*dy[dd];
          if(tx==0 || ty==0 || tx==R+1 || ty==C+1) break;
          if(c[tx][ty]=='.')continue;
          else 
          {
            ok=true;
            break;
          }
        }
        if(ok)continue;
        for(int tt=0;tt<4;tt++) if(dd!=tt)
        {
          for(int k=1;;k++)
          {
            int tx,ty;
            tx=i+k*dx[tt];
            ty=j+k*dy[tt];
            if(tx==0 || ty==0 || tx==R+1 || ty==C+1) break;
            if(c[tx][ty]=='.')continue;
            else 
            {
              ok=true;
              break;
            }
          }
          if(ok)break;
        }
        if(ok) ans++;
        else pos=false;
      }
      if(!pos)break;
    }
    if(pos) printf("%d\n",ans);
    else printf("IMPOSSIBLE\n");
  }
  return 0;
}

