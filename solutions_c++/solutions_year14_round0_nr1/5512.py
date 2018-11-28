//shjj-magic

#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

int h1[30],h2[30],A,B;

int check()
{
int _s=0,x=0;
for (int i=1;i<=16;i++)
  if (h1[i]==A&&h2[i]==B) _s++,x=i;
if (_s>1) return -1;
return x;
}

int main()
{
freopen("magic.in","r",stdin);
freopen("magic.out","w",stdout);
int Test,tt=0;scanf("%d",&Test);
for (;Test--;)
  {
  scanf("%d",&A);
  for (int i=1;i<=4;i++)
    for (int j=1;j<=4;j++){int x;scanf("%d",&x);h1[x]=i;}
  scanf("%d",&B);
  for (int i=1;i<=4;i++)
    for (int j=1;j<=4;j++){int x;scanf("%d",&x);h2[x]=i;}
  int gg=check();
  if (gg<0) printf("Case #%d: Bad magician!\n",++tt);
  if (!gg) printf("Case #%d: Volunteer cheated!\n",++tt);
  if (gg>0) printf("Case #%d: %d\n",++tt,gg);
  }
}