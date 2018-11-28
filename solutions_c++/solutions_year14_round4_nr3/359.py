#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define  Maxn  100000+50
#define Maxm  1000000+50
#define oo 2000000000
    int flow[Maxm],capa[Maxm],node[Maxm],edge[Maxn],next[Maxm];
    int dist[Maxn],Q[Maxn];
    int work[Maxn];
class flow_Graph{
    
public:
    int n,m;
    int src,dest,edgenum;
    flow_Graph(int a){
        n = a;
        edgenum = 0;
        for (int i=0;i<=a;edge[i++] = -1);
    }
    void insert(int a,int b,int c1,int c2){
        node[edgenum] = b,flow[edgenum] = 0,capa[edgenum] = c1;
        next[edgenum] = edge[a],edge[a] = edgenum++;
        node[edgenum] = a,flow[edgenum] = 0,capa[edgenum] = c2;
        next[edgenum] = edge[b],edge[b] = edgenum++;
    }
    bool bfs(){
        int low = 0,high = 1;
        memset(dist,-1,sizeof(dist));
        for (dist[src] = 0,Q[low] = src;low<high;low++)
            for (int now = Q[low],i = edge[now];i!=-1;i = next[i])
                if (flow[i]<capa[i]&&dist[node[i]]<0)
                {
                    dist[node[i]] = dist[now]+1;
                    Q[high++] = node[i];
                }
            if (dist[dest]<0) return false;
            else return true;
    }
    int dfs(int now,int edit){
        if (now==dest) return edit;
        for (int &i = work[now],tmp;i!=-1;i = next[i])
            if (flow[i]<capa[i]&&dist[node[i]] == dist[now]+1&&(tmp = dfs(node[i],min(edit,capa[i]-flow[i])))>0)
            {
                flow[i]+=tmp;
                flow[i^1]-=tmp;
                return tmp;
            }
        return 0;
    }
    int dinic(int _src,int _dest){
        src = _src,dest = _dest;
        int res = 0;
        while(bfs()){
            for (int i=0;i<=n;i++)
                work[i] = edge[i];
            while(1){
                int tmp = dfs(src,oo);
                if (tmp==0) break;
                res +=tmp;
            }
        }
        return res;
    }
};
#define In(x) ((x)*2)
#define Out(x) ((x)*2+1)
int W,H,mat[110][510];
inline int isin(int x,int y){
    return x>=0&&x<W&&y>=0&&y<H;
}
int main()
{
    int tt;
    int i,N,j;
    int B,x0,y0,x1,y1;
    freopen("4.in","r",stdin), freopen("4.out","w",stdout);
    scanf("%d",&tt);
    for (int tcas = 1; tcas<= tt; tcas++){
        scanf("%d%d%d",&W,&H,&B);
        memset(mat,0,sizeof(mat));
        for (int t = 0;t<B;t++){
            scanf("%d%d%d%d",&x0, &y0, &x1, &y1);
            for (i = x0;i<=x1; i++)
                for (j = y0; j<=y1;j ++)
                    mat[i][j] = 1;
        }
        flow_Graph G(W*H*2+10);
        for (i = 0; i<W;i++)
            for (j =0;j<H;j++)
            if (mat[i][j]==0){
                int in = In(i*H+j), out = Out(i*H+j);
                
                G.insert(in, out, 1, 0);
                if (isin(i-1, j)&&mat[i-1][j]==0){
                    int in2 = In((i-1)*H+j);
                    G.insert(out, in2, 1,0);
                }
                if (isin(i+1, j)&&mat[i+1][j]==0){
                    int in2 = In((i+1)*H+j);
                    G.insert(out, in2, 1,0);
                }
                if (isin(i, j+1)&&mat[i][j+1]==0){
                    int in2 = In((i)*H+j+1);
                    G.insert(out, in2, 1,0);
                }
                if (isin(i, j-1)&&mat[i][j-1]==0){
                    int in2 = In((i)*H+j-1);
                    G.insert(out, in2, 1,0);
                }
                
            }
        int src = In(W*H), dest  = Out(W*H);
        for (i = 0;i<W;i++){
            int in = In(i*H);
            G.insert(src, in, 1, 0);
            int out = Out(i*H+H-1);
            G.insert(out, dest, 1,0);
        }
        int ans = G.dinic(src,dest);
        printf("Case #%d: %d\n", tcas, ans);
       // printf("%d\n",G.edgenum);
    }
}
        
                
                
    
