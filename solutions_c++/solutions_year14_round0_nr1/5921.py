#include<stdio.h>
int T,a[40][40];
int q[10],h,t;
int C;
FILE *out = fopen("output.txt","w");

int main()
{
	scanf("%d",&T);
	while(T--)
	{
		C++;

		int before,after;
		scanf("%d",&before);
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		for(int i=1;i<=4;i++)
		{
			q[i] = a[before][i];
		}
		scanf("%d",&after);
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		int cnt=0,dap=0;
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				if(q[i]==a[after][j])
				{
					cnt++;
					dap = q[i];
					break;
				}
			}
		}
		if(cnt==1)
		{
			printf("Case #%d: %d\n",C,dap);
		}
		if(cnt==0)
		{
			printf("Case #%d: Volunteer cheated!\n",C);
		}
		if(cnt>=2)
		{
					printf("Case #%d: Bad magician!\n",C);
	

		}

	}
	return 0;
}