#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
#include <vector>
using namespace std;
typedef long long ll;

int n;
int G[1005];
vector<int> Gr[1005];

int dis[1005];
int timing[1005];
int dfs(int p,int t){
    if(dis[G[p]]>0){
        if(timing[G[p]]!=t)return 0;
        return dis[p]-dis[G[p]]+1;
    }
    dis[G[p]]=dis[p]+1;
    timing[G[p]]=t;
    return dfs(G[p],t);
}

int d[1005];
int maxlen(int p,int q){
    if(d[p]>=0)return d[p];
    d[p]=0;
    for(int i=0;i<Gr[p].size();i++){
        if(Gr[p][i]!=q){
            d[p]=max(d[p],maxlen(Gr[p][i],q)+1);
        }
    }
    return d[p];
}

int main(){
    freopen("C-large.in","r",stdin);
    freopen("clarge.txt","w",stdout);
    int T,Case=1;
    for(scanf("%d",&T);Case<=T;Case++){
        memset(dis,0,sizeof(dis));
        memset(d,-1,sizeof(d));
        memset(timing,0,sizeof(timing));
        scanf("%d",&n);
        for(int i=0;i<=n+1;i++)Gr[i].clear();
        for(int i=1;i<=n;i++){
            scanf("%d",&G[i]);
            Gr[G[i]].push_back(i);
        }
        
        int ans=0;
        for(int i=1;i<=n;i++){
            if(!dis[i]){
                ans=max(ans,dfs(i,i));
            }
        }
        int ans2=0;
        for(int i=1;i<=n;i++){
            if(d[i]<0 && G[G[i]]==i){
                ans2+=maxlen(i,G[i])+maxlen(G[i],i)+2;
            }
        }
        
        printf("Case #%d: %d\n",Case,max(ans,ans2));
    }
    return 0;
}

