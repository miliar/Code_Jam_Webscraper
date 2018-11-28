#include<cstdio>

int r,c,a[110][110],Ans,NoAns,
	dx[]={0,-1,0,1},dy[]={-1,0,1,0},f[5];

int main()
{
	int TestCase,Case,i,j,I,J,k;
	//freopen("a.in","rb",stdin);
	//freopen("a.out","wb",stdout);
	scanf("%d",&TestCase);
	for(Case=1;Case<=TestCase;Case++)
	{
		scanf("%d%d",&r,&c);
		for(i=0;i<r;i++)
			for(scanf("\n"),j=0;j<c;j++)
				a[i][j]=getchar();
		Ans=NoAns=0;
		for(i=0;i<r;i++)
			for(j=0;j<c;j++)
			if(a[i][j]!='.')
			{
				for(k=0;k<4;k++)
				{
					I=i;J=j;
					for(;;)
					{
						I+=dx[k];
						J+=dy[k];
						if(I<0||I>=r||J<0||J>=c)
						{
							f[k]=0;
							break;
						}
						if(a[I][J]!='.')
						{
							f[k]=1;
							break;
						}
					}
				}
				if(a[i][j]=='<')k=0;
				if(a[i][j]=='^')k=1;
				if(a[i][j]=='>')k=2;
				if(a[i][j]=='v')k=3;
				if(!f[k])Ans++;
				if(!f[0]&&!f[1]&&!f[2]&&!f[3])
					NoAns=1;
			}
		if(NoAns)
			printf("Case #%d: IMPOSSIBLE\n",Case);
		else
			printf("Case #%d: %d\n",Case,Ans);
	}
	return 0;
}
