/* ***********************************************
Author        :kuangbin
Created Time  :2015/5/30 23:26:37
File Name     :F:\ACM\2015ACM\比赛练习\2015GCJ_R2\C.cpp
************************************************ */

#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <time.h>
using namespace std;
vector<int>vec[220];
map<string,int>mp;
char str[100010];
char ss[110];


const int MAXN = 100010;//点数的最大值
const int MAXM = 400010;//边数的最大值
const int INF = 0x3f3f3f;
struct Edge
{
	int to,next,cap,flow;
}edge[MAXM];//注意是MAXM
int tol;
int head[MAXN];
int gap[MAXN],dep[MAXN],pre[MAXN],cur[MAXN];
void init()
{
	tol = 0;
	memset(head,-1,sizeof(head));
}
//加边，单向图三个参数，双向图四个参数
void addedge(int u,int v,int w,int rw=0)
{
	edge[tol].to = v;edge[tol].cap = w;edge[tol].next = head[u];
	edge[tol].flow = 0;head[u] = tol++;
	edge[tol].to = u;edge[tol].cap = rw;edge[tol].next = head[v];
	edge[tol].flow = 0;head[v]=tol++;
}
//输入参数：起点、终点、点的总数
//点的编号没有影响，只要输入点的总数
int sap(int start,int end,int N)
{
	memset(gap,0,sizeof(gap));
	memset(dep,0,sizeof(dep));
	memcpy(cur,head,sizeof(head));
	int u = start;
	pre[u] = -1;
	gap[0] = N;
	int ans = 0;
	while(dep[start] < N)
	{
		if(u == end)
        {
            int Min = INF;
            for(int i = pre[u];i != -1; i = pre[edge[i^1].to])
                if(Min > edge[i].cap - edge[i].flow)
                        Min = edge[i].cap - edge[i].flow;
            for(int i = pre[u];i != -1; i = pre[edge[i^1].to])
            {
                edge[i].flow += Min;
                edge[i^1].flow -= Min;
            }
            u = start;
            ans += Min;
            continue;
        }
        bool flag = false;
        int v;
        for(int i = cur[u]; i != -1;i = edge[i].next)
        {
            v = edge[i].to;
            if(edge[i].cap - edge[i].flow && dep[v]+1 == dep[u])
            {
                flag = true;
                cur[u] = pre[v] = i;
                break;
            }
        }
        if(flag)
        {
            u = v;
            continue;
        }
        int Min = N;
        for(int i = head[u]; i != -1;i = edge[i].next)
            if(edge[i].cap - edge[i].flow && dep[edge[i].to] < Min)
            {
                Min = dep[edge[i].to];
                cur[u] = i;
            }
        gap[dep[u]]--;
        if(!gap[dep[u]])return ans;
        dep[u] = Min+1;
        gap[dep[u]]++;
        if(u != start) u = edge[pre[u]^1].to;
	}
	return ans;
}


int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
	int iCase = 0;
	scanf("%d",&T);
	int n;
	while(T--){
		iCase++;
		scanf("%d",&n);
		gets(str);
		mp.clear();
		int cnt = 0;
		for(int i = 0;i < n;i++){
			vec[i].clear();
			gets(str);
			char *p = strtok(str," ");
			while(p){
				sscanf(p,"%s",ss);
				p = strtok(NULL," ");
				if(mp.find(ss) == mp.end())
					mp[ss] = ++cnt;
				vec[i].push_back(mp[ss]);
			}
		}
		init();
		for(int i = 0;i < vec[0].size();i++)
			addedge(0,2*vec[0][i]-1,INF);
		for(int i = 0;i < vec[1].size();i++)
			addedge(2*vec[1][i],2*cnt+1,INF);
		for(int i = 1;i <= cnt;i++)
			addedge(2*i-1,2*i,1);
		//for(int i = 2;i < n;i++)
			//addedge(2*cnt+1 + 2*(i-1)-1,2*cnt+1+2*(i-1),INF);
		for(int i = 2;i < n;i++){
			int sz = vec[i].size();
			for(int j = 0;j < sz;j++)
				for(int k = j+1;k < sz;k++){
					addedge(2*vec[i][k],2*vec[i][j]-1,INF);
					addedge(2*vec[i][j],2*vec[i][k]-1,INF);
				}
		}
		printf("Case #%d: %d\n",iCase,sap(0,2*cnt+1,2*cnt+2));
	}
    return 0;
}
