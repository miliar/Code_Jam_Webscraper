#include<cstdio>
#include<iostream>
#include<string>
#include<cstring>
#include<vector>
using namespace std;
#define pb push_back
const int N=1100;
struct Edge {
    int v,next;
    Edge(int v=-1,int next=-1):v(v),next(next){}
}e[N*2];
int head[N],total;
void init(){
    memset(head,-1,sizeof(head));total=0;
}
void adde(int u,int v){
    e[total]=Edge(v,head[u]);head[u]=total++;
}
int ee[N];
int sz[N];

int dfs(int u,int f){
    sz[u]=1;
    for(int i=head[u];i!=-1;i=e[i].next){
        int v=e[i].v;if(v==f)continue;
        dfs(v,u);
        sz[u]=max(sz[u],sz[v]+1);
    }
    return sz[u];
}
int vis[N];int sta[N],top;
int main(){
    #ifdef DouBi
    freopen("in.cpp","r",stdin);
    freopen("out.cpp","w",stdout);
    #endif // DouBi
    int T;scanf("%d",&T);
    int cas=1;
    while(T--){
        int n;scanf("%d",&n);
        init();
        for(int i=1;i<=n;i++){
            scanf("%d",&ee[i]);
            adde(i,ee[i]);adde(ee[i],i);
        }
        //printf("%d\n",n);for(int i=1;i<=n;i++)printf("%d ",ee[i]);printf("\n");
        memset(vis,0,sizeof(vis));memset(sz,0,sizeof(sz));
        int ans=0,bns=0;
        for(int i=1;i<=n;i++){
            if(!vis[i]){
                top=0;
                int j=i;
                while(!vis[j]){
                    sta[top++]=j;vis[j]=i;j=ee[j];
                }
                if(vis[j]!=i)continue;
                else {
                    for(int k=0;k<top;k++){
                        if(sta[k]==j){
                                if(top-k>2){
                                    ans=max(ans,top-k);
                                }
                                else {
                                    int x=dfs(sta[top-1],sta[top-2]),y=dfs(sta[top-2],sta[top-1]);
                                    bns+=x+y;
                                }
                        }
                    }
                }
            }
        }
        printf("Case #%d: %d\n",cas++,max(ans,bns));
//        int cns=ans;
//        bns=0,ans=0;
//        for(int i=1;i<=n;i++){
//            memset(vis,0,sizeof(vis));
//            int j=i;top=0;
//                while(!vis[j]){
//                    sta[top++]=j;vis[j]=i;j=ee[j];
//                }
//                for(int k=0;k<top;k++){
//                    if(sta[k]==j){
//                        if(top-k>2){
//                            ans=max(ans,top-k);
//                        }
//                        else {
//                            int x=dfs(sta[top-1],sta[top-2]),y=dfs(sta[top-2],sta[top-1]);
//                            bns+=x+y;
//                        }
//                    }
//                }
//        }
        //printf("Case #%d: %d\n",cas++,ans==cns);
        //if(ans!=cns)printf("%d %dasdfasdf\n",ans,cns);
    }
    return 0;
}
