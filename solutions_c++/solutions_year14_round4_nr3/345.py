#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<queue>
using namespace std;

int first[100010],next[1000000],end[1000000],wi[1000000];
int map[1001][1001],tot,pre[100010],prd[100010];
int ss,tt;
int c[4]={0,0,1,-1};
int d[4]={1,-1,0,0};

void add_edge(int x,int y,int s){
	next[++tot]=first[x];
	first[x]=tot;
	end[tot]=y;
	wi[tot]=s;
}

void add(int x,int y,int s){
	//printf("%d %d\n",x,y);
	add_edge(x,y,s);
	add_edge(y,x,0);
}

queue<int> que;
int bo[100010];

int bfs(int x){
	que.push(x);
	for (int i=1; i<=tt; ++i) bo[i]=0;
	bo[x]=1;
	while (!que.empty()){
		int x=que.front(); que.pop();
		for (int k=first[x]; k!=-1; k=next[k])
			if (wi[k] && !bo[end[k]]){
				bo[end[k]]=1;
				que.push(end[k]);
				pre[end[k]]=x;
				prd[end[k]]=k;
			}
	}
	if (!bo[tt]) return 0;
	for (int X=tt; X!=x; X=pre[X]){
		wi[prd[X]]-=1;
		wi[prd[X]^1]+=1;
	}
	return 1;
}

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T,ca=0;
	scanf("%d",&T);
	while (T--){
		int n,W,H;
		scanf("%d%d%d",&W,&H,&n);
		memset(map,0,sizeof(map));
		for (int i=1; i<=n; ++i){
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			++x1,++y1,++x2,++y2;
			for (int k=x1; k<=x2; ++k)
				for (int l=y1; l<=y2; ++l)
					map[k][l]=1;
		}
		ss=2*W*H+1;
		tt=ss+1;
		tot=-1;
		memset(first,-1,sizeof(first));
		for (int i=1; i<=W; ++i){
			if (map[i][1]) continue;
			add(ss,i,1);
		}
		for (int i=1; i<=W; ++i){
			if (map[i][H]) continue;
			add(W*H+(H-1)*W+i,tt,1);
		}
		for (int i=1; i<=H; ++i)
			for (int j=1; j<=W; ++j){
				if (map[j][i]) continue;
				for (int k=0; k<4; ++k){
					int xx=i+c[k],yy=j+d[k];
					if (xx<1 || xx>H || yy<1 || yy>W || map[yy][xx]) continue;
					add((i-1)*W+j+H*W,(xx-1)*W+yy,1);
				}
			}
		for (int i=1; i<=W*H; ++i) add(i,i+W*H,1);
		int ans=0;
		for (int i=1; i<=W; ++i){
			if (map[i][1]) continue;
			ans+=bfs(i);
		}
		printf("Case #%d: %d\n",++ca,ans);
	}
	return 0;
}
