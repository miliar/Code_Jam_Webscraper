#include <stdio.h>

int main()
{
	int tcase;
	int x,y,xnum[5][5],ynum[5][5];
	int cnt,re;

	FILE *in,*out;
	in=fopen("A-small-attempt0.in","r");
	out=fopen("output.txt","w");

	fscanf(in,"%d",&tcase);
	for(int t=0;t<tcase;t++)
	{
		fscanf(in,"%d",&x);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
				fscanf(in,"%d",&xnum[i][j]);
		}

		fscanf(in,"%d",&y);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
				fscanf(in,"%d",&ynum[i][j]);
		}
		cnt=0;

		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(xnum[x-1][i]==ynum[y-1][j])
				{
					cnt++;
					re=xnum[x-1][i];
				}
			}
		}

		fprintf(out,"Case #%d: ",t+1);
		if(cnt==1)
			fprintf(out,"%d\n",re);
		else if(cnt==0)
			fprintf(out,"Volunteer cheated!\n");
		else
			fprintf(out,"Bad magician!\n");
	}

	return 0;
}