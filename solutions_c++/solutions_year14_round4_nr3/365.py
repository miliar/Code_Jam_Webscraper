#include<cstdio>
#include<cstring>
#include<algorithm>
#include<ctype.h>
#include<iostream>
#include<map>
#define MAXD 100010
#define MAXM 800010
#define INF 0x3f3f3f3f
using namespace std;
int N, M, first[MAXD], e, next[MAXM], v[MAXM], flow[MAXM];
int S, T, d[MAXD], q[MAXD], work[MAXD];
bool vis[110][510];

void add(int x, int y, int z)
{
    v[e] = y, flow[e] = z;
    next[e] = first[x], first[x] = e ++;
}

void init()
{
    int W,H,B,x,y;
    scanf("%d%d%d",&W,&H,&B);
    N=W*H;S=0,T=N*2+1;
    memset(first,-1,sizeof(first[0])*(T+2));e=0;
    memset(vis,false,sizeof vis);
    for(int i=0;i<B;++i){
		int a1,b1,a2,b2;
		scanf("%d%d%d%d",&a1,&b1,&a2,&b2);
		++a1,++b1,++a2,++b2;
		for(int x=a1;x<=a2;++x)
			for(int y=b1;y<=b2;++y) vis[x][y]=true;
    }
	for(int i=1;i<=W;++i)
		for(int j=0;j<H;++j)
			if(!vis[i][j+1]) add(j*W+i,j*W+i+N,1),add(j*W+i+N,j*W+i,0);
	//Êú
	for(int j=1;j<=W;++j){
		for(int i=0;i<H-1;++i){
			if(vis[j][i+1] || vis[j][i+2]) continue;
			add(j+W*i+N,(i+1)*W+j,1),add((i+1)*W+j,j+W*i+N,0);
			//cout<<j<<' '<<i+1<<"->"<<j<<' '<<i+2<<endl;
		}
		for(int i=H-1;i>0;--i){
			if(vis[j][i+1] || vis[j][i]) continue;
			add(j+W*i+N,(i-1)*W+j,1),add((i-1)*W+j,j+W*i+N,0);
			//cout<<j<<' '<<i+1<<"->"<<j<<' '<<i<<endl;
		}
	}
	//ºá
	for(int i=0;i<H;++i){
		for(int j=1;j<W;++j){
			if(vis[j][i+1] || vis[j+1][i+1]) continue;
			add(j+W*i+N,j+W*i+1,1),add(j+W*i+1,j+W*i+N,0);
			//cout<<j<<' '<<i+1<<"->"<<j+1<<' '<<i+1<<endl;
		}
		for(int j=W;j>1;--j){
			if(vis[j][i+1] || vis[j-1][i+1]) continue;
			add(j+W*i+N,j+W*i-1,1),add(j+W*i-1,j+W*i+N,0);
			//cout<<j<<' '<<i+1<<"->"<<j-1<<' '<<i+1<<endl;
		}
	}

	for(int i=1;i<=W;++i){
		if(vis[i][1]) continue;
		add(S,i,1),add(i,S,1);
		//cout<<"S->"<<i<<' '<<'1'<<endl;
	}
	for(int i=1;i<=W;++i){
		if(vis[i][H]) continue;
		add(W*(H-1)+i+N,T,1),add(T,W*(H-1)+i+N,1);
		//cout<<i<<' '<<H<<"->T"<<endl;
	}
	N=T+1;
}

int bfs()
{
    int i, j, rear = 0;
    memset(d, -1, sizeof(d[0]) * (N + 1));
    d[S] = 0, q[rear ++] = S;
    for(i = 0; i < rear; i ++)
        for(j = first[q[i]]; j != -1; j = next[j])
            if(flow[j] && d[v[j]] == -1)
            {
                d[v[j]] = d[q[i]] + 1, q[rear ++] = v[j];
                if(v[j] == T) return 1;
            }
    return 0;
}

int dfs(int cur, int a)
{
    if(cur == T) return a;
    for(int &i = work[cur]; i != -1; i = next[i])
        if(flow[i] && d[v[i]] == d[cur] + 1)
            if(int t = dfs(v[i], min(a, flow[i])))
            {
                flow[i] -= t, flow[i ^ 1] += t;
                return t;
            }
    return 0;
}

int dinic()
{
    int ans = 0, t;
    while(bfs())
    {
        memcpy(work, first, sizeof(first[0]) * (N + 1));
        while(t = dfs(S, INF))
            ans += t;
    }
    return ans;
}

int main()
{
	freopen("C-small-attempt0.in","rb",stdin);
	freopen("test.out","wb",stdout);
	int T,cas=1;scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",cas++);
		init();
		int x=dinic();
		printf("%d\n",x);
	}
	return 0;
}
