#include <stdio.h>
const int MAXN=15;
const int MAXPOT=1050;
int n,p;
int pd[MAXN][MAXPOT][2];
int fazpd(int num,int v,int ver)
{
	if(pd[num][v][ver]==-1)
	{
		int pe=v;
		int ga=(1<<num)-pe-1;
		if(ver==0)
		{
			if(ga==0)
			{
				pd[num][v][ver]=(1<<num);
			}
			else
			{
				ga=(ga-1)/2;
				pe=(1<<(num-1))-ga-1;
				pd[num][v][ver]=fazpd(num-1,pe,0);
			}
		}
		else
		{
			if(pe==0)
			{
				pd[num][v][ver]=1;
			}
			else
			{
				pe=(pe-1)/2;
				pd[num][v][ver]=(1<<(num-1))+fazpd(num-1,pe,1);
			}
		}
	}
	return pd[num][v][ver];
}
int main()
{
	for(int i=0;i<=10;i++)
	{
		int jmax=(1<<i)-1;
		for(int j=0;j<=jmax;j++)
		{
			pd[i][j][0]=-1;
			pd[i][j][1]=-1;
		}
		pd[i][0][0]=1;
		pd[i][0][1]=1;
	}
	int t;
	scanf("%d",&t);
	for(int w=1;w<=t;w++)
	{
		scanf("%d %d",&n,&p);
		int pot=(1<<n);
		int g=0;
		int ng=0;
		for(int i=0;i<pot;i++)
		{
			int x=fazpd(n,i,0);
			int y=fazpd(n,i,1);
			if(y<=p) g=i;
			if(x<=p) ng=i;
		}
		printf("Case #%d: %d %d\n",w,g,ng);
	}
	return 0;
}
