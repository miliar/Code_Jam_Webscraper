#include <stdio.h>

FILE *in=fopen("input.txt","r");
FILE *out=fopen("output.txt","w");

int n,m[2];
int a[2][4][4];
int cnt;

int main()
{
	fscanf(in,"%d",&n);

	for(int i=0;i<n;i++)
	{
		int t;

		cnt=0;

		for(int j=0;j<2;j++)
		{
			fscanf(in,"%d",&m[j]);
			for(int k=0;k<4;k++)
			{
				for(int p=0;p<4;p++)
					fscanf(in,"%d",&a[j][k][p]);
			}
		}

		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(a[0][m[0]-1][j]==a[1][m[1]-1][k])
				{
					t=a[0][m[0]-1][j];
					cnt++;
				}
			}
		}
			
		fprintf(out,"Case #%d: ",i+1);
		if(cnt==0)
			fprintf(out,"Volunteer cheated!\n");
		else if(cnt==1)
			fprintf(out,"%d\n",t);
		else
			fprintf(out,"Bad magician!\n");
	}

	return 0;
}