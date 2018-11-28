#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#define oo 1000000000
using namespace std;
struct graph{
    int Go[5000005],Next[5000005],Now[10005],R[5000005],bs;
    void clear(){
        memset(Now,0,sizeof(Now));
        bs=1;
    }
    void add(int x,int y,int c){
        bs++;
        Go[bs]=y;
        R[bs]=c;
        Next[bs]=Now[x];
        Now[x]=bs;
        bs++;
        Go[bs]=x;
        R[bs]=0;
        Next[bs]=Now[y];
        Now[y]=bs;
    }
}G;
map <string,int> M;
char st[1000005],po[10005];
vector <int> F;
int dis[10005],DL[10005];
void bfs(int SS){
    memset(dis,0xff,sizeof(dis));
    int h=0,t=1;
    DL[1]=SS;
    dis[SS]=0;
    do{
        h++;
        for(int i=G.Now[DL[h]];i;i=G.Next[i]){
            if(G.R[i]>0&&(dis[G.Go[i]]==-1||dis[G.Go[i]]>dis[DL[h]]+1)){
                dis[G.Go[i]]=dis[DL[h]]+1;
                t++;
                DL[t]=G.Go[i];
            }
        }
    }while(h<t);
//    for(int i=1;i<=20;i++)printf("%d ",dis[i]);
//    printf("\n");
}
int TT;
int dfs(int p,int r){
//    printf("%d\n",p);
    if(p==TT)return r;
    int k=r;
    for(int i=G.Now[p];i;i=G.Next[i]){
        int j=G.Go[i];
        if(G.R[i]&&dis[j]==dis[p]+1){
            int t=dfs(j,min(k,G.R[i]));
            k-=t;
            G.R[i]-=t;
            G.R[i^1]+=t;
            if(k==0)break;
        }
    }
    if(k==r)dis[p]=-1;
    return r-k;
}
int main(){
    int T,tt,n,m,i,j,k,l,ans;
    int SS=8001;
    scanf("%d",&T);
    for(tt=1;tt<=T;tt++){
        G.clear();
        M.clear();
        scanf("%d\n",&n);
        int gs=0;
        for(i=1;i<=n;i++){
//        printf("!!%d\n",i);
            gets(st);
//    printf("%s\n",st);
            j=0;
            F.clear();
            while(st[j]){
                sscanf(st+j,"%s",po);
                j+=strlen(po);
                while(st[j]==' ')j++;
//            printf("%s\n",po);
                if(M.count(po)){
                    F.push_back(M[po]);
                }else {
                    gs++;
                    M.insert(make_pair((string)po,gs));
                    F.push_back(M[po]);
                }
            }
//            for(j=0;j<F.size();j++)printf("%d\n",F[j]);
//    printf("!!%d\n",i);
            if(i==1){
                for(j=0;j<F.size();j++)G.add(SS,F[j],oo);
            }
            if(i==2){
                for(j=0;j<F.size();j++)G.add(F[j]+4000,TT,oo);
            }
            for(j=0;j<F.size();j++)
                for(k=0;k<F.size();k++)
                    if(F[j]!=F[k]){
                        G.add(F[j]+4000,F[k],oo);
                    }
        }
        for(i=1;i<=gs;i++)G.add(i,i+4000,1);
        ans=0;
        while(1){
//            printf("!\n");
            bfs(SS);
            if(dis[TT]==-1)break;
            i=dfs(SS,oo);
            if(i==0)break;
            ans+=i;
        }
        printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}
