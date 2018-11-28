// Round1A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include "iostream"
#include "vector"
#include "algorithm"
#include "stdio.h"
#include "string"
#include "string.h"
using namespace std;

int G[55][55]={};
int skipped = 0;

void print(int N)
{
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<N;j++) cout<<G[i][j]<<" ";
		cout<<endl;
	}
	cout<<endl;
}
int dfs(vector<vector<int> > &g, int x, int y, int N, int cur, int dir, int skip)
{
	if(x==N && y==N && skip==0) return 1;
	if(skip)
	{
		if(x<N){
		int ret = dfs(g,x+1,y,N,cur,0,0);
		if(ret!=0) { skipped = x; return ret;}
		ret = dfs(g,x+1,y,N,cur,1,0);
		if(ret!=0) { skipped = x; return ret;}
		}
		if(y<N){
		int ret = dfs(g,x,y+1,N,cur,0,0);
		if(ret!=0) { skipped = N+y; return ret;}
		ret = dfs(g,x,y+1,N,cur,1,0);
		if(ret!=0) { skipped = N+y; return ret;}
		}
	}
	if(x+y==N*2 || cur==g.size() ) return 0;
	if(dir)
	{
		if(x<N)
		{
			for(int i=0;i<N;i++)
			{
				//check consistence
				if(G[x][i]!=0 && G[x][i]!=g[cur][i]){
					return 0;
				}
				//check increase order
				if(x && G[x-1][i] >= g[cur][i]){
					return 0;
				}
			}
			vector<int> r;
			for(int i=0;i<N;i++)
			{
				r.push_back(G[x][i]);
				G[x][i]=g[cur][i];
			}
			int ret = dfs(g,x+1,y,N,cur+1,0,skip);
			if(ret!=0) return ret;
			ret = dfs(g,x+1,y,N,cur+1,1,skip);
			if(ret!=0) return ret;
			for(int i=0;i<N;i++)
				G[x][i]=r[i];
		}
	}
	else 
	{
		if(y<N)
		{
			for(int i=0;i<N;i++)
			{
				//check consistence
				if(G[i][y]!=0 && G[i][y]!=g[cur][i]){
					return 0;
				}
				//check increase order
				if(y && G[i][y-1] >= g[cur][i]){
					return 0;
				}
			}
			vector<int> r;
			for(int i=0;i<N;i++)
			{
				r.push_back(G[i][y]);
				G[i][y]=g[cur][i];
			}
			int ret = dfs(g,x,y+1,N,cur+1,0,skip);
			if(ret!=0) return ret;
			ret = dfs(g,x,y+1,N,cur+1,1,skip);
			if(ret!=0) return ret;
			for(int i=0;i<N;i++)
				G[i][y]=r[i];
		}
	}

	return 0;
}
vector<int> solve()
{
	int N;
	vector<vector<int> > g;
	cin>>N;
	for(int i=0;i<N*2-1;i++)
	{
		vector<int> x(N);
		for(int j=0;j<N;j++)
		{
			cin>>x[j];
		}
		g.push_back(x);
	}
	sort(g.begin(),g.end());
	memset(G,0,sizeof(G));
	skipped = -1;
	int x = dfs(g,0,0,N,0,0,1);
	int y = dfs(g,0,0,N,0,1,1);
	vector<int> ret;

	if(skipped >= N)
	{
		for(int i=0;i<N;i++)
			ret.push_back(G[i][skipped-N]);
	}
	else 
	{
		for(int i=0;i<N;i++)
			ret.push_back(G[skipped][i]);
	}
	return ret;
}

int main()
{
	int T;
	cin>>T;
	for(int tc=0;tc<T;tc++)
	{
		vector<int> ret = solve();
		cout<<"Case #"<<tc+1<<":";
		for(int i=0;i<ret.size();i++)
		{
			cout<<" "<<ret[i];
		}
		cout<<endl;
	}
	return 0;
}

