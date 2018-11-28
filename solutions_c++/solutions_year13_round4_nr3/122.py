#include <cstdio>
#include <cstring>

int n;
int a[2200], b[2200], c[2200];
int ed[2200][2200];
int vi[2200];
int T;
void dfs(int nu)
{
	int du[2200];
	int aj, now=n;
	memset(du, 0, sizeof du);
	for (int i=0;i<n;++i)
		for (int j=0;j<n;++j)
			if (ed[i][j])
				du[j]++;
	for (int i=0;i<n;++i)
	{
		for (int j=n-1;j>=0;--j)
		{
			if (du[j]==0)
			{
				aj = j;
				break;
			}
		}
		//printf("%d\n", aj);
		vi[aj]=--now;
		for (int j=0;j<n;++j)
			if (ed[aj][j])--du[j];
		--du[aj];
	}
}
int main()
{
	scanf("%d", &T);
	for (int I=1;I<=T;++I)
	{
		scanf("%d", &n);
		for (int i=0;i<n;++i)
			scanf("%d", &a[i]);
		for (int i=0;i<n;++i)
			scanf("%d", &b[i]);
		memset(ed, 0, sizeof ed);
		for (int i=0;i<n;++i)
		{
			for (int j=i-1;j>=0;--j)
				if (a[j]>=a[i])
					ed[j][i]=1;
			for (int j=i-1;j>=0;--j)
				if (a[j]+1==a[i])
				{
					ed[i][j]=1;
					break;
				}
			for (int j=i+1;j<n;++j)
				if (b[j]>=b[i])
					ed[j][i]=1;
			for (int j=i+1;j<n;++j)
				if (b[j]+1==b[i])
				{
					ed[i][j]=1;
					break;
				}
		}
		for (int i=0;i<n;++i)
			if (a[i]==1 && b[i]==1)
				dfs(i);
		printf("Case #%d:", I);
		for (int i=0;i<n;++i)
			printf(" %d", vi[i]+1);
		printf("\n");
	}
}
