#include<cstdio>
bool judge(int N,int M,int h[][105],int rowMax[],int colMax[])
{
	for(int i=0;i<N;++i)
	{
		for(int j=0;j<M;++j)
		{
			if(h[i][j]<rowMax[i]&&h[i][j]<colMax[j])
				return false;
		}
	}
	return true;
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int nCase=1;nCase<=T;++nCase)
	{
		int N,M;
		scanf("%d%d",&N,&M);
		int h[105][105];
		int rowMax[105]={},colMax[105]={};
		for(int i=0;i<N;++i)
		{
			for(int j=0;j<M;++j)
			{
				scanf("%d",&h[i][j]);
				if(h[i][j]>rowMax[i])
				{
					rowMax[i]=h[i][j];
				}
				if(h[i][j]>colMax[j])
				{
					colMax[j]=h[i][j];
				}
			}
		}
		printf("Case #%d: %s\n",nCase,judge(N,M,h,rowMax,colMax)?"YES":"NO");
	}
	return 0;
}
