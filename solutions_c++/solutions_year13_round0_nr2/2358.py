#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;

int yk[105],tt[105];
int in[105][105];

void solve()
{
	int n,m;
	scanf("%d %d",&n,&m);
	memset(yk,0,sizeof(yk));
	memset(tt,0,sizeof(tt));
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			scanf("%d",&in[i][j]);
			yk[i]=max(yk[i],in[i][j]);
			tt[j]=max(tt[j],in[i][j]);
		}
	}
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			if(in[i][j]<yk[i]&&in[i][j]<tt[j])
			{
				printf("NO\n");
				return;
			}
		}
	}
	printf("YES\n");
	return;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
