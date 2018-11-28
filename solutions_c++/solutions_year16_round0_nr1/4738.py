#include <stdio.h>

int main(void)
{
	int T,i,j;
	FILE *in=fopen("A-large.in","r");
	FILE *out=fopen("outal.txt","w");

	fscanf(in,"%d",&T);

	for(i=1;i<=T;i++)
	{
		int arr[10]={0},cur=0;
		int m;

		fscanf(in,"%d",&m);

		if(!m)
		{
			fprintf(out,"Case #%d: INSOMNIA\n",i);
			continue;
		}

		for(j=m;cur<10;j+=m)
		{
			int n=j;

			while(n)
			{
				int y=n%10;
				n/=10;

				if(!arr[y])
				{
					arr[y]++;
					cur++;
				}
			}
		}

		fprintf(out,"Case #%d: %d\n",i,j-m);
	}

	fclose(in);
	fclose(out);

	return 0;
}