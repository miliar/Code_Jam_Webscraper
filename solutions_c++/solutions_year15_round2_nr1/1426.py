#include<stdio.h>
#include<vector>
#include<queue>
#define MAX 1000000

using namespace std;

int dist[MAX+10];

queue <int> q;

void bfs(int s);
int rev(int a);

int rev(int a)
{
	int d=0;
	while(a>0)
	{
		d=d*10 +(a%10);
		a/=10;
	}
	return d;
}

void bfs(int s)
{
	int u,v;
	dist[s]=1;
	q.push(s);
	while(!q.empty())
	{
		u=q.front();
		q.pop();
		if(u>MAX)
			continue;
		v=u+1;
		if(dist[v]==-1)
		{
			dist[v]=dist[u]+1;
			q.push(v);
			v = rev(u);
			if(dist[v]==-1)
			{
				dist[v]=dist[u]+1;
				q.push(v);
				v = rev(u);
				
			}
			
		}
	}

}


int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	memset(dist,-1,sizeof(dist));
	q.empty();
	bfs(1);
	int t,ti,i;
	int n;
	scanf("%d",&t);
	for(ti=1; ti<=t; ++ti)
	{
		scanf("%d",&n);
		printf("Case #%d: %d\n",ti,dist[n]);
	}
	return 0;
}