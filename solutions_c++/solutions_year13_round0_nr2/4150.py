#include<stdio.h>
#include<algorithm>

using namespace std;

int mat[110][110];
int fin[110][110];

int main()
{
	int T;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++)
	{
		int n,m;
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
				scanf("%d",&mat[i][j]);
		}
		for(int i=0;i<n;i++)
		{
			int mayor=-1;
			for(int j=0;j<m;j++)
				mayor=max(mayor,mat[i][j]);
			for(int j=0;j<m;j++)
				fin[i][j]=mayor;
		}
		for(int i=0;i<m;i++)
		{
			int mayor=-1;
			for(int j=0;j<n;j++)
				mayor=max(mayor,mat[j][i]);
			for(int j=0;j<n;j++)
				fin[j][i]=min(mayor,fin[j][i]);
		}
		bool eq=true;
		for(int i=0;i<n&&eq;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(mat[i][j]!=fin[i][j])
				{
					eq=false;
					break;
				}
			}
		}
		printf("Case #%d: ",cs);
		if(eq)	printf("YES\n");
		else		printf("NO\n");
	}
	return 0;
}
