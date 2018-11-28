#include <stdio.h>
#include <string.h>
const int MAXN = 105;
int map[MAXN][MAXN];
int maxr[MAXN],maxc[MAXN];

int main()
{
	FILE* fp = fopen("B-large.in","r");
	FILE* fp1 = fopen("B-large.out","w");
	int T;
	int n,m;
	fscanf(fp,"%d",&T);
	for(int c = 1;c <= T;c++)
	{
		fscanf(fp,"%d %d",&n,&m);
		int i,j;
		for(i = 1;i <= n;i++)
			for(j = 1;j <= m;j++)
				fscanf(fp,"%d",&map[i][j]);
		
		memset(maxr,0,sizeof(maxr));
		for(i = 1;i <= n;i++)
			for(j = 1;j <= m;j++)
				if(map[i][j] > maxr[i])
					maxr[i] = map[i][j];

		memset(maxc,0,sizeof(maxc));
		for(j = 1;j <= m;j++)
			for(i = 1;i <= n;i++)
				if(map[i][j] > maxc[j])
					maxc[j] = map[i][j];

		bool flag = 1;
		for(i = 1;i <= n && flag;i++)
			for(j = 1;j <= m && flag;j++)
				if(map[i][j] < maxr[i] && map[i][j] < maxc[j])
					flag = false;

		if(flag)
		{
			fprintf(fp1,"Case #%d: YES\n",c);
		}
		else
		{
			fprintf(fp1,"Case #%d: NO\n",c);
		}
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}
