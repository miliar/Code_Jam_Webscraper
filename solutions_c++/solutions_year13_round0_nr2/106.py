#include<cstdio>

const int HMAX=100;
const int WMAX=100;

int H,W,a[HMAX][WMAX];

bool solve()
{
	while(H>0||W>0)
	{
		int i,j,ii,jj,kk=2147483647;
		for(i=0;i<H;i++)for(j=0;j<W;j++)if(a[i][j]<kk)kk=a[ii=i][jj=j];
		for(j=0;j<W;j++)if(a[ii][j]!=kk)break;
		if(j==W)
		{
			H--;
			for(j=0;j<W;j++)a[ii][j]=a[H][j];
			continue;
		}
		for(i=0;i<H;i++)if(a[i][jj]!=kk)break;
		if(i==H)
		{
			W--;
			for(i=0;i<H;i++)a[i][jj]=a[i][W];
			continue;
		}
		return false;
	}
	return true;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int s=1;s<=t;s++)
	{
		scanf("%d%d",&H,&W);
		for(int i=0;i<H;i++)
			for(int j=0;j<W;j++)
				scanf("%d",&a[i][j]);
		printf("Case #%d: %s\n",s,(solve()?"YES":"NO"));
	}
	return 0;
}
