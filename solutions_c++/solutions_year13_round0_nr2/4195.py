#include <stdio.h>
#include <algorithm>
using namespace std;
const int MAXN=110;
int t;
int n,m;
int mat[MAXN][MAXN];
int maior[2][MAXN];
int main()
{
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++)
	{
		scanf("%d %d",&n,&m);
		for(int i=1;i<=n;i++) maior[0][i]=0;
		for(int i=1;i<=m;i++) maior[1][i]=0;
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=m;j++)
			{
				scanf("%d",&mat[i][j]);
				maior[0][i]=max(maior[0][i],mat[i][j]);
				maior[1][j]=max(maior[1][j],mat[i][j]);
			}
		}
		int resp=1;
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=m;j++)
			{
				if(maior[0][i]>mat[i][j] && maior[1][j]>mat[i][j]) resp=0;
			}
		}
		printf("Case #%d: ",caso);
		if(resp) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
