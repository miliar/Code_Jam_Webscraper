#include <stdio.h>
#include <string.h>

int main()
{
	FILE *in,*out;
	in = fopen("A-large.in","r");
	out = fopen("A_large.out","w");
	int smax,num,need,i,j,t,layer;
	int a[1001];
	char c;
	fscanf(in,"%d",&t);
	for (layer=0;layer<t;layer++)
	{
		//input data
		fscanf(in,"%d",&smax);
		fscanf(in,"%c",&c);
		for (i=0;i<=smax;i++)
		{
			fscanf(in,"%c",&c);
			a[i] = c-48;
		}
		//compute the NEED friend number
		num = a[0]; need = 0;
		for (i=1;i<=smax;i++)
		{
			if (num<i)
			{
				need = need + i-num;
				num = i;
			}
			num = num + a[i];
		}
		fprintf(out,"Case #%d: %d\n",layer+1,need);
	}
	fclose(in);
	fclose(out);
	return 0;
}
