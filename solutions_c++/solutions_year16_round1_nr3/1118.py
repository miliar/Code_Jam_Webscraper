#include<bits/stdc++.h>
using namespace std;
int fr[1005];
int vis[1005];
int dis[1005];
int tym;
int ans;
int cyclen;
int line;
vector<int>rev[1005];

int findlen(int x, int y)
{
      int ret=1,tmp;
      for(int i=0; i<rev[x].size(); i++){
          int v=rev[x][i];
          if(v!=y){
              tmp=findlen(v,y);
              ret=max(ret,1+tmp);
          }
      }
      return ret;
}

void dfs(int x)
{
      dis[x]=++tym;
      vis[x]=1;
      int v=fr[x];
      if(!vis[v])
            dfs(v);
      else{
              if(vis[v]==1){
                //printf("Cycle found\n");
                //printf("%d:%d %d:%d\n",v,dis[v],x,dis[x]);
                int len = 1+abs(dis[x]-dis[v]);
                if(len>2)
                     cyclen=max(cyclen,len);
                else if(len==2){
               //      printf("here %d %d\n",x,v);
                     int xx=findlen(x,v);
                     int vv=findlen(v,x);
                     line+=(xx+vv);
                }

              }
      }
      vis[x]=2;
}

int main()
{
       int T,it,N,i,j,a;
       freopen("C-large.in","r",stdin);
       freopen("C.out","w",stdout);
       scanf("%d",&T);
       for(it=1; it<=T; it++)
       {
             scanf("%d",&N);

             for(i=0; i<=N; i++)  rev[i].clear();

             for(i=1; i<=N; i++)
             {
                 scanf("%d",&fr[i]);
                 rev[fr[i]].push_back(i);
             }

             for(i=0; i<=N; i++)  vis[i]=0;
             tym=0;
             ans=0;
             cyclen=0;
             line=0;
           //  printf("%d\n",findlen(10,3));

             for(i=1; i<=N; i++){
                  if(!vis[i]){
                       dfs(i);
                  }
             }

             ans=max(cyclen,line);
             printf("Case #%d: %d\n",it,ans);
       }
       return 0;
}
