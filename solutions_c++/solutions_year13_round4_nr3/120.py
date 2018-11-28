#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cassert>
#include <queue>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);i++)

typedef long long ll;

int A[2001];
int B[2001];

int adj[2001][2001];
int deg[2001];
int r[2001];
int used[2001];

int main()
{
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++)
	{
		int n;
		scanf("%d",&n);
		REP(i,n)
			scanf("%d",&A[i]);
		REP(i,n)
			scanf("%d",&B[i]);
		memset(adj,0,sizeof(adj));
		for(int i=0;i<n;i++)
		{
			int maxid=-1;
			for(int j=0;j<i;j++)
			{
				if(A[j]>=A[i])
				{
					//rj > ri
					adj[j][i]=1;
				}
				else if(A[j]==A[i]-1)
				{
					// attach longest
					maxid=j;
				}
				else // A[j]<A[i]-1
				{
					// no information
				}
			}
			if(A[i]!=1)
			{
				assert(maxid>=0);
				// i > maxid
				adj[i][maxid]=1;
			}
		}
		for(int i=0;i<n;i++)
		{
			int maxid=-1;
			for(int j=n-1;j>i;j--)
			{
				if(B[j]>=B[i])
				{
					//rj > ri
					adj[j][i]=1;
				}
				else if(B[j]==B[i]-1)
				{
					// attach longest
					maxid=j;
				}
				else // B[j]<B[i]-1
				{
					// no information
				}
			}
			if(B[i]!=1)
			{
				assert(maxid>=0);
				// i > maxid
				adj[i][maxid]=1;
			}
		}

		memset(deg,0,sizeof(deg));
		memset(used,0,sizeof(used));
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				deg[i]+=adj[i][j];
		priority_queue<int, vector<int>, greater<int> > q;
		for(int i=0;i<n;i++)
			if(deg[i]==0)
			{
				q.push(i);
				used[i]=1;
			}
		int val=1;
		while(!q.empty())
		{
			int cur=q.top(); q.pop();
			r[cur]=val++;
			for(int i=0;i<n;i++)
			{
				deg[i]-=adj[i][cur];
				assert(deg[i]>=0);
				if(deg[i]==0 && !used[i])
				{
					used[i]=1;
					q.push(i);
				}
			}
		}
		assert(val==n+1);
		printf("Case #%d:",test);
		for(int i=0;i<n;i++)
		{
			printf(" %d",r[i]);
		}
		puts("");
	}
	return 0;
}
