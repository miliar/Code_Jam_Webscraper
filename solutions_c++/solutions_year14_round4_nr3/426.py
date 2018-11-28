//
//  main.cpp
//  ttt
//
//  Created by Ningchen Ying on 5/31/14.
//  Copyright (c) 2014 Ningchen Ying. All rights reserved.
//

#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>

using namespace std;
#define  Maxn  100100+5
#define Maxm  1000100+5
#define oo 2000000000

int dinic_f[Maxm],dinic_C[Maxm],dinic_G[Maxm],dinic_E[Maxn],dinic_N[Maxm];
int dist[Maxn],Q[Maxn];
int remarks[Maxn];
class flow_Graph{
    
public:
    int n,m;
    int src,dest,totCnt;
    flow_Graph(int a){
        n = a;
        totCnt = 0;
        for (int i=0;i<=a;dinic_E[i++] = -1);
    }
    void insert(int a,int b,int c1,int c2){
        dinic_G[totCnt] = b,dinic_f[totCnt] = 0,dinic_C[totCnt] = c1;
        dinic_N[totCnt] = dinic_E[a],dinic_E[a] = totCnt++;
        dinic_G[totCnt] = a,dinic_f[totCnt] = 0,dinic_C[totCnt] = c2;
        dinic_N[totCnt] = dinic_E[b],dinic_E[b] = totCnt++;
    }
    bool bfs(){
        int low = 0,high = 1;
        memset(dist,-1,sizeof(dist));
        for (dist[src] = 0,Q[low] = src;low<high;low++)
            for (int now = Q[low],i = dinic_E[now];i!=-1;i = dinic_N[i])
                if (dinic_f[i]<dinic_C[i]&&dist[dinic_G[i]]<0)
                {
                    dist[dinic_G[i]] = dist[now]+1;
                    Q[high++] = dinic_G[i];
                }
        if (dist[dest]<0) return false;
        else return true;
    }
    int dfs(int now,int edit){
        if (now==dest) return edit;
        for (int &i = remarks[now],tmp;i!=-1;i = dinic_N[i])
            if (dinic_f[i]<dinic_C[i]&&dist[dinic_G[i]] == dist[now]+1&&(tmp = dfs(dinic_G[i],min(edit,dinic_C[i]-dinic_f[i])))>0)
            {
                dinic_f[i]+=tmp;
                dinic_f[i^1]-=tmp;
                return tmp;
            }
        return 0;
    }
    int dinic(int _src,int _dest){
        src = _src,dest = _dest;
        int res = 0;
        while(bfs()){
            for (int i=0;i<=n;i++)
                remarks[i] = dinic_E[i];
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
int W,H,matrix_m[110][510];
inline int isin(int x,int y){
    return x>=0&&x<W&&y>=0&&y<H;
}

void solve(int ca){
    int N;
    int B,x0,y0,x1,y1;
    cin>>W>>H>>B;
    memset(matrix_m,0,sizeof(matrix_m));
    for (int t = 0;t<B;t++){
        scanf("%d%d%d%d",&x0, &y0, &x1, &y1);
        for (int i = x0;i<=x1; i++){
            for (int j = y0; j<=y1;j ++){
                matrix_m[i][j] = 1;
            }
        }
    }
    flow_Graph ync(W*H*2+10);
    for (int i = 0; i<W;i++){
        for (int j =0;j<H;j++){
            if (matrix_m[i][j]==0){
                int in = In(i*H+j), out = Out(i*H+j);
                ync.insert(in, out, 1, 0);
                if (isin(i-1, j)&&matrix_m[i-1][j]==0){
                    int tp = In((i-1)*H+j);
                    ync.insert(out, tp, 1,0);
                }
                if (isin(i+1, j)&&matrix_m[i+1][j]==0){
                    int tp = In((i+1)*H+j);
                    ync.insert(out, tp, 1,0);
                }
                if (isin(i, j+1)&&matrix_m[i][j+1]==0){
                    int tp = In((i)*H+j+1);
                    ync.insert(out, tp, 1,0);
                }
                if (isin(i, j-1)&&matrix_m[i][j-1]==0){
                    int tp = In((i)*H+j-1);
                    ync.insert(out, tp, 1,0);
                }
                
            }
        }
    }
    int src = In(W*H), dest  = Out(W*H);
    for (int i = 0;i<W;i++){
        int in = In(i*H);
        ync.insert(src, in, 1, 0);
        int out = Out(i*H+H-1);
        ync.insert(out, dest, 1,0);
    }
    int ans = ync.dinic(src,dest);
    printf("Case #%d: %d\n", ca, ans);
}

int main()
{
    int T;
    freopen("/Users/YNingC/Documents/CodeForces/ttt/ttt/C-small-attempt0.in","r",stdin);
    freopen("/Users/YNingC/Documents/CodeForces/ttt/ttt/C-small-attempt0.out","w", stdout);
    cin>>T;
    for (int ca = 1; ca<= T; ca++){
        solve(ca);
    }
    return 0;
}
