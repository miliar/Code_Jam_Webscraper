#include<algorithm>
#include<cstdio>
#include<cstring>

using namespace std;

int vis[10];
int i,n,t,c,ca,cas;

int Check(int x){

int f,i;

  f=1;

  while (x){
    vis[x % 10]=1;
    x/=10;
  }

  for (i=0;i<10;i++) f&=vis[i];
  return f;

}

int main(){

  freopen("A_l.in","r",stdin);
  freopen("A_l.out","w",stdout);
  scanf("%d",&ca);
  cas=0;
  while (ca--){
    cas++;
    scanf("%d",&n);
    if (n==0){
      printf("Case #%d: INSOMNIA\n",cas);
      continue;
    }
    memset(vis,0,sizeof(vis));
    c=n;
    while (!Check(c)){
      c+=n;
    }
    printf("Case #%d: %d\n",cas,c);
  }

  return 0;

}

