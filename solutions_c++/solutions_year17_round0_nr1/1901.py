#include <cstdio>
#include <cstring>
#include <algorithm>
#define MAXN 2000

char V[MAXN];
bool rot[MAXN];

void solve()
{
  int ans=0,K;
  bool apr=false;
  scanf("%s%d",V,&K);
  std::fill(rot,rot+MAXN,false);
  int N=strlen(V);
  for(int x=0;V[x]>32;x++)
  {
    apr^=rot[x];
    bool act=(V[x]=='-');
    act^=apr;
    if(!act)continue;
    if(x+K>N){printf("IMPOSSIBLE\n");return;}
    ans++;
    apr^=1;
    rot[x+K]^=1;
  }
  printf("%d\n",ans);
}

int main()
{
  int T;
  scanf("%d\n",&T);
  for(int i=1;i<=T;i++){printf("Case #%d: ",i);solve();}
}
