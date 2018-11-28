#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <memory.h>

using namespace std;

#define INF 2140000000
#define MAX_V 130005
struct edge{        // to : 목적지, c : 용량 , r: 역변 정보 : ad[i][j] 의 역엣지 = ad[ad[i][j].to][ad[i][j].r]
	int to,c,r;  
};

int n,w,h;
int b[1005][1005];

vector<edge> ad[MAX_V]; // 그래프 인접리스트
bool chk[MAX_V];		// DFS에서 방문 체크

void add_edge(int v1,int v2,int c){
	edge e1={v2,c,ad[v2].size()};
	ad[v1].push_back(e1);
	edge e2={v1,0,ad[v1].size()-1};
	ad[v2].push_back(e2);
}

int DFS(int s,int t,int f){  // s -> t 경로탐색
	if(s==t) return f;
	chk[s]=true;
	for(int i=0;i<ad[s].size();i++){
		edge &now=ad[s][i];
		if(now.c>0 && !chk[now.to]){
			int ret=DFS(now.to,t,min(f,now.c));
			if(ret>0){
				now.c-=ret;
				ad[now.to][now.r].c+=ret;
				return ret;
			}
		}
	}
	return 0;
}

int network_flow(int s,int t){ // s->t 최대흐름
	int ret=0,flow=-1;
	while(flow!=0){
		memset(chk,0,sizeof(chk));
		flow=DFS(s,t,INF);
		ret+=flow;
	}
	return ret;
}

// 최소 절단 :{ 잔여그래프에서 s에서 갈 수 있는 정점} - {갈 수 없는 정점} 사이의 간선
int dx[5]={0,1,0,-1,};
int dy[5]={1,0,-1,0,};


int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,ca=0;
	scanf("%d",&t);
	while(t--){
		scanf("%d %d %d",&w,&h,&n);
		for(int i=0;i<h;i++) for(int j=0;j<w;j++) b[i][j]=0;
		for(int i=0;i<n;i++){
			int x0,y0,x1,y1;
			cin>>x0;
			cin>>y0;
			cin>>x1;
			cin>>y1;
			for(int j=x0;j<=x1;j++) for(int k=y0;k<=y1;k++)
				b[k][j]++;
		}
		int V=130000;
		for(int i=0;i<130000;i++) ad[i].clear();
		for(int i=0;i<h;i++) for(int j=0;j<w;j++){
			if(b[i][j]==0){
				add_edge(2*(i*w+j+1),2*(i*w+j+1)+1,1);
				if(i==0) add_edge(0,2*(i*w+j+1),1);
				if(i==h-1) add_edge(2*(i*w+j+1)+1,V-1,1);
				for(int k=0;k<4;k++){
					int x=i+dx[k],y=j+dy[k];
					if(x>=0 && x<h && y>=0 && y<w && b[x][y]==0)
						add_edge(2*(i*w+j+1)+1,2*(x*w+y+1),1);
				}
			}
		}
		printf("Case #%d: %d\n",++ca,network_flow(0,V-1));
	}
	return 0;
}