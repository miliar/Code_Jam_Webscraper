#include <stdio.h>
#include <stdlib.h>

int map[102][102];

int main()
{
	int t,tcase;
	int n,m,i,j,min,minx,miny;
	int chk;

	FILE *in,*out;
	in=fopen("B-large.in","r");
	out=fopen("output.out","w");

	fscanf(in,"%d",&tcase);

	for(t=0;t<tcase;t++)
	{
		fprintf(out,"Case #%d: ",t+1);
		fscanf(in,"%d%d",&n,&m);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
				fscanf(in,"%d",&map[i][j]);
		}

		while(1)
		{
			min=101;
			for(i=0;i<n;i++)
			{
				for(j=0;j<m;j++)
				{
					if(min>map[i][j] && map[i][j]>0)
					{
						min=map[i][j];
						minx=i;
						miny=j;
					}
				}
			}
			if(min==101)
			{
				fprintf(out,"YES\n");
				break;
			}
			chk=0;
			for(i=0;i<n;i++)
			{
				if(map[i][miny]!=0 && map[i][miny]!=min)
				{
					chk=1;
					break;
				}
			}
			if(chk==0)
			{
				for(i=0;i<n;i++)
					map[i][miny]=0;
			}
			else
			{
				chk=0;
				for(i=0;i<m;i++)
				{
					if(map[minx][i]!=0 && map[minx][i]!=min)
					{
						chk=1;
						break;
					}
				}
				if(chk==0)
				{
					for(i=0;i<m;i++)
						map[minx][i]=0;
				}
				else
				{
					fprintf(out,"NO\n");
					break;
				}
			}
		}
	}

	return 0;
}