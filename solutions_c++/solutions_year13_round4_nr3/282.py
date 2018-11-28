#include <stdio.h>
int x[2010][2],way[2010];
int n;
bool find(int y)
{
	if(y==n+1)return 1;
	int now[2010][2];
	int i,max0=0;
	for(i=0;i<n;i++)
		if(way[i])
			now[i][0]=x[i][0],now[i][1]=x[i][1];
	for(i=0;i<n;i++)
		if(!way[i])now[i][0]=max0+1;
		else if(now[i][0]>max0)max0=now[i][0];
	max0=0;
	for(i=n-1;i>=0;i--)
		if(!way[i])now[i][1]=max0+1;
		else if(now[i][1]>max0)max0=now[i][1];
	for(i=0;i<n;i++)
		if(!way[i]&&x[i][0]==now[i][0]&&x[i][1]==now[i][1])
		{
			way[i]=y;
			if(find(y+1))return 1;
			else way[i]=0;
		}
		return 0;
}
int main()
{
	int t,j,i;
	unsigned long long now;
	FILE *in= fopen("b.in","r");
	FILE *out= fopen("b.out","w");
	fscanf(in,"%d",&t);
	for(j=1;j<=t;j++)
	{
		fscanf(in,"%d",&n);
		for(i=0;i<n;i++)
			fscanf(in,"%d",&x[i][0]),way[i]=0;
		for(i=0;i<n;i++)
			fscanf(in,"%d",&x[i][1]);
		find(1);
		fprintf(out,"Case #%d:",j);
		for(i=0;i<n;i++)
			fprintf(out," %d",way[i]);
		fprintf(out,"\n");
		printf("1");
	}
	
	for(i=1;i<8;i++)
	return 0;
}
