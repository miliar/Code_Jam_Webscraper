#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <iostream>
using namespace std;

struct edge{
	int to,cap,rev;
}p;
vector <edge> v[100005];
int level[100005],iter[100005];

void bfs(int st){
	memset(level,-1,sizeof(level));
	queue <int> q;
	level[st] = 0;
	q.push(st);
	while(!q.empty()){
		int now = q.front();	q.pop();
		for(int i=0;i<v[now].size();i++){
			if(v[now][i].cap>0 && level[v[now][i].to]<0){
				level[v[now][i].to] = level[now]+1;
				q.push(v[now][i].to);
			}
		}
	}
}

int dfs(int now,int ed,int f){
	if(now==ed)
		return f;
	for(int &i = iter[now];i<v[now].size();i++){
		if(v[now][i].cap>0 && level[now]<level[v[now][i].to]){
			int tmp = dfs(v[now][i].to,ed,min(f,v[now][i].cap));
			if(tmp>0){
				v[now][i].cap -= tmp;
				v[v[now][i].to][v[now][i].rev].cap += tmp;
				return tmp;
			}
		}
	}
	return 0;
}

int flow(int st,int ed){
	int ret = 0;
	while(1){
		bfs(st);
		if(level[ed]<0)
			return ret;
		memset(iter,0,sizeof(iter));
		int f;
		while((f = dfs(st,ed,1e9))>0)
			ret += f;
	}
}
void add_edge(int from,int to,int cap){
	v[from].push_back((edge){to,cap,v[to].size()});
	v[to].push_back((edge){from,0,v[from].size()-1});
}

int ss[505][105],op[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int T;
    scanf(" %d",&T);
    for(int t=0,N,M,B;t<T && scanf(" %d %d %d",&M,&N,&B)==3;t++){
        memset(ss,0,sizeof(ss));
        for(int x1,x2,y1,y2,i=0;i<B && scanf(" %d %d %d %d",&y1,&x1,&y2,&x2)==4;i++)
            for(int i=x1;i<=x2;i++)
                for(int j=y1;j<=y2;j++)
                    ss[i][j] = 1;
        /*for(int i=0;i<N;i++){
            for(int j=0;j<M;j++)
                printf("%d",ss[i][j]);
            printf("\n");
        }*/
        for(int i=0;i<100005;i++)
            v[i].clear();
        for(int i=0;i<M;i++){
            if(ss[0][i]==0)
                add_edge(0,i+1,1);
            if(ss[N-1][i]==0)
                add_edge((N-1)*M+i+1+N*M,2*N*M+1,1);
        }
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                if(ss[i][j]==0){
                    add_edge(i*M+j+1,i*M+j+1+N*M,1);
                    for(int k=0;k<4;k++){
                        int nx = i+op[k][0], ny = j+op[k][1];
                        if(nx>=0 && nx<N && ny>=0 && ny<M && ss[nx][ny]==0){
                            add_edge(i*M+j+1+N*M,nx*M+ny+1,1);
                        }
                    }
                }
            }
        }
        printf("Case #%d: %d\n",t+1,flow(0,N*M*2+1));
    }

    return 0;
}
