#include<iostream>
#include<cstdio>
#include<queue>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;

bool vis[1<<22];
map<int,int> keys[1<<22];
vector<int> k[100];
int need[100];
int N;

void bfs(vector<int>& res)
{
	res.clear();
	vector<int> q,p,who;
	q.push_back(0);
	p.push_back(0);
	who.push_back(0);
	bool ok = 0;
	for(int I=0;!ok && I<(int)q.size();I++)
	{
		int x = q[I];
		for(int i=1;i<=N;i++)
			if(!( x & (1<<i) ) && keys[x][need[i]] )
			{
				int nx = x|(1<<i);
				if( vis[nx]) continue;
				vis[nx] = 1;
				keys[nx] = keys[x];
				keys[nx][need[i]]--;
				for(int j=0;j<(int)k[i].size();++j)
					keys[nx][k[i][j]]++;
				q.push_back(nx);
				p.push_back(I);
				who.push_back(i);
				if( nx == ((1<<N)-1)<<1)
				{
					ok = 1;
					break;
				}
			}
	}
	if(ok)
	{
		int x = p.size()-1;
		while(x)
		{
			res.push_back(who[x]);
			x = p[x];
		}
		reverse(res.begin(),res.end());
	}
}
int main()
{
	freopen("in.txt","rt",stdin);
	freopen("out_D.txt","wt",stdout);
	int TC;
	scanf("%d",&TC);
	int kk,x;
	for(int tc =1; tc<=TC;tc++)
	{
		cerr<<tc<<endl;
		memset(vis,0,sizeof(vis));
		for(int i=0;i<1<<22;i++)
			keys[i].clear();
		for(int i=0;i<100;i++)
		{
			k[i].clear();
			need[i] = 0;
		}
		scanf("%d%d",&kk,&N);
		for(int i=0;i<kk;i++)
		{
			scanf("%d",&x);
			k[0].push_back(x);
			keys[0][x]++;
		}
		for(int i=0;i<N;i++)
		{
			scanf("%d %d",&need[i+1],&kk);
			for(int j=0;j<kk;j++)
			{
				scanf("%d",&x);
				k[i+1].push_back(x);
			}
		}
		vector<int> v;
		bfs(v);
		printf("Case #%d:",tc);
		if(v.size())
		{
			for(int i=0;i<v.size();i++)
				printf(" %d",v[i]);
		}
		else
		{
			printf(" IMPOSSIBLE");
		}
		printf("\n");
	}
	return 0;
}