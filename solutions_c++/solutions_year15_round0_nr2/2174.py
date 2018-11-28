#include<stdio.h>
#include<queue>

using namespace std;
int F[1005];
int main()
{
	FILE *in=fopen("1.in","r");
	FILE *out=fopen("1.out","w");
	int TT;
	fscanf(in,"%d",&TT);
	for(int t=1;t<=TT;t++)
	{
		int D;
		int max=0;
		fscanf(in,"%d",&D);
		for(int i=0;i<D;i++)
		{
			fscanf(in,"%d",&F[i]);
			if(max<F[i])max=F[i];
		}
		int ans=max;
		for(int i=1;i<=max;i++)
		{
			int cnt=0;
			for(int j=0;j<D;j++)
			{
				if(F[j]>i)
				{
					cnt += (F[j]-1)/i;
				}
			}
			if(cnt+i<ans)ans=cnt+i;
		}
		fprintf(out,"Case #%d: %d\n",t,ans);
	}
}