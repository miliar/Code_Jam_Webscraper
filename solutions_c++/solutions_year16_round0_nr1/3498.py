#include <bits/stdc++.h>

using namespace std;

bool vis[11];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,u,c,y,j;
    long long int x,a;
    scanf("%d",&j);
    for(t=1;t<=j;t++)
    {
        memset(vis,0,sizeof(vis));
        scanf("%lld",&a);
        if(a==0){
            printf("Case #%d: INSOMNIA\n",t);
  continue;
  }
  c=0;
  x=a;
  u=1;
    while(c<10)
    {
        a=x*u;
        while(a>0){
      y=a%10;
      if(vis[y]==0){
      vis[y]=1;
      c++;
      }
      a=a/10;
    }
    u++;
    }
    u--;
  printf("Case #%d: %lld\n",t,x*u);
    }
    return 0;
}
