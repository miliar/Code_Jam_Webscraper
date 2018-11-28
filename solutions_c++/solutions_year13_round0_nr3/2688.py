#include <cstdio>
#include <cstring>

int a[1010];
int b[20];

inline bool check(int x)
{
  if (x<=9) return true;
  int l,i;
  l=0;
  while (x>0)
  {
    b[l]=x%10;
    x/=10;
    l++;
  }
  i=0;
  l--;
  while (i<l)
  {
    if (b[i]!=b[l]) return false;
    i++;
    l--;
  }
  return true;
}

inline void init()
{
  int i;
  memset(a,0,sizeof(a));
  for (i=1;i*i<=1000;i++)
  {
    if (check(i))
      if (check(i*i))
        a[i*i]++;
  }
  for (i=1;i<=1000;i++)
    a[i]+=a[i-1];
}

int main()
{
  int T,o,x,y;
  freopen("C-small-attempt0.in","r",stdin);
  freopen("C1.txt","w+",stdout);
  init();
  scanf("%d",&T);
  for (o=1;o<=T;o++)
  {
    scanf("%d%d",&x,&y);
    printf("Case #%d: %d\n",o,a[y]-a[x-1]);
  }
  return 0;
}
