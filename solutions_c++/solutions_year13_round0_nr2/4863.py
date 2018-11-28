#include <stdio.h>
#include <string.h>

using namespace std;

int d[200][200];
int n,m;

int test()
{
	for (int i=1;i<=n;i++)
		for (int j=1;j<=m;j++)
			if (d[i][j] < d[0][j] && d[i][j] < d[i][0]) return 0;
	return 1;
}

int main()
{
	int T;
	freopen("/Users/zpl/Documents/Codes/gcj_pre2/input.txt","r",stdin);
	freopen("/Users/zpl/Documents/Codes/gcj_pre2/output.txt","w",stdout);
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		scanf("%d%d",&n,&m);
		memset(d,0,sizeof(d));
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++)
            {
				scanf("%d",&d[i][j]);
				if (d[i][j] >= d[i][0]) d[i][0]=d[i][j];
				if (d[i][j] >= d[0][j]) d[0][j]=d[i][j];
            }
		printf("Case #%d: ",t);
		if (test()) printf("YES\n");
		else printf("NO\n");
	}
}
