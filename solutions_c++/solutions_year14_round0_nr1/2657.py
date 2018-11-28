#include <iostream>
#include <cstdio>

using namespace std;

int T;
int s[8][8];
int a[9],b[9];

int main()
{
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);

  scanf("%d",&T);
  for(int cas=1;cas<=T;cas++)
  {
    int tt;
    scanf("%d",&tt);
    for(int i=1;i<=4;i++)
      for(int j=1;j<=4;j++)
        scanf("%d",&s[i][j]);
    for(int i=1;i<=4;i++)
      a[i]=s[tt][i];
    scanf("%d",&tt);
    for(int i=1;i<=4;i++)
      for(int j=1;j<=4;j++)
        scanf("%d",&s[i][j]);
    for(int i=1;i<=4;i++)
      b[i]=s[tt][i];

    int same(0),ans;
    for(int i=1;i<=4;i++)
      for(int j=1;j<=4;j++)
        if(a[i]==b[j])
        {
          same++;
          ans=a[i];
        }
    printf("Case #%d: ",cas);
    if(0==same)
    {
      printf("Volunteer cheated!\n");
      continue;
    }
    if(1==same)
    {
      printf("%d\n",ans);
      continue;
    }
    if(1<same)
    {
      printf("Bad magician!\n");
      continue;
    }
  }
  return 0;
}

