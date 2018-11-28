#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

struct eugin
{
  int x,y,t;
};

int n,m,up;
eugin a[10010];
int r[110];
int c[110];

bool operator < (eugin q,eugin w)
{
  if (q.t>w.t) return true;
  return false;
}

inline bool work()
{
  int i,x,y;
  for (i=1;i<=up;i++)
  {
    x=a[i].x;
    y=a[i].y;
    if (r[x]==0 || c[y]==0)
    {
      if (r[x]==0) r[x]=a[i].t;
      if (c[y]==0) c[y]=a[i].t;
      continue;
    }
    if (a[i].t==r[x] || a[i].t==c[y])
      continue;
    return false;
  }
  return true;
}

int main()
{
  int T,o,i,j;
  freopen("B-large.in","r",stdin);
  freopen("B2.txt","w+",stdout);
  scanf("%d",&T);
  for (o=1;o<=T;o++)
  {
    up=0;
    scanf("%d%d",&n,&m);
    for (i=1;i<=n;i++)
      for (j=1;j<=m;j++)
      {
        up++;
        scanf("%d",&a[up].t);
        a[up].x=i;
        a[up].y=j;
      }
    sort(a+1,a+1+up);
    memset(r,0,sizeof(r));
    memset(c,0,sizeof(c));
    printf("Case #%d: ",o);
    if (work())
      puts("YES");
    else
      puts("NO");
  }
  return 0;
}
