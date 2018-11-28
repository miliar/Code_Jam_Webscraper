#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE *in,*out;
	in = fopen("B-large.in","r");
	out = fopen("Blarge.out","w");

	int t,layer,d,i,j,max,ans,special;
	int p[10000];
	fscanf(in,"%d",&t);
	for (layer=1; layer<=t; layer++)
	{
		fscanf(in,"%d",&d);
		max = 0;
		for (i=0; i<d;i++) 
		{
			fscanf(in,"%d",&p[i]);
			if (max<p[i]) max = p[i];
		}
		ans = max;
		for (i = max; i>0; i--)
		{
			special = 0;
			for (j=0;j<d;j++)
			{
				if (p[j]>i)
				{
					special+= p[j]/i;
					if (p[j]%i==0)
						special--;
				}
			}
			if (i+special<ans)
				ans = i+special;
		}
		fprintf(out,"Case #%d: %d\n",layer,ans);
	}
	fclose(in);
	fclose(out);
	return 0;
}