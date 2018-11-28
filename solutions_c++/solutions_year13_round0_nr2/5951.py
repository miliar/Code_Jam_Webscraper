#include <stdio.h>


int M[110][110];
bool ch(int n, int m)
{	
	int i,j,x,y;
	bool a,b;
	
	for (i=1; i<=n; i++) {
		a=false,b=false;
		for (j=1; j<=m; j++) {
			for (x=1; x<=n; x++)
				if (M[x][j] > M[i][j]) a=true;
			for (y=1; y<=m; y++)
				if (M[i][y] > M[i][j]) b=true;
		}
		if (a && b) return false;
	}
	return true;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,k=0;
	scanf("%d",&t);

	while (++k<=t)
	{
		printf("Case #%d: ",k);
		int i,j;
		int n,m;
		scanf("%d%d",&n,&m);

		for (i=1; i<=n; i++)
			for (j=1; j<=m; j++)
				scanf("%d",M[i]+j);
		printf("%s\n",(ch(n,m))?"YES":"NO");

	}
}
