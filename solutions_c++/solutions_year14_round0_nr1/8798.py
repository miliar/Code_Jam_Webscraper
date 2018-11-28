#include <stdio.h>
using namespace std;
FILE *in,*out;
int main()
{
	in = fopen("in.txt","r");
	out = fopen("out.txt","w");
	int t;
	int a[4][4],r,b[16],c,z,d;
	fscanf(in,"%d",&t);
	for(int i=1;i<=t;i++)
	{
		z=0;
		for (int j=0;j<16;j++) b[j]=0;
		fscanf(in,"%d",&r);
		for (int j=0;j<4;j++) for (int k=0;k<4;k++)
		{
			fscanf(in,"%d",&c);
			if (j==r-1) b[c-1]++;
		}
		fscanf(in,"%d",&r);
		for (int j=0;j<4;j++) for (int k=0;k<4;k++)
		{
			fscanf(in,"%d",&c);
			if (j==r-1) b[c-1]++;
		}
		for (int j=0;j<16;j++) if (b[j]==2)
		{
			d=j+1;
			z++;
		}
		if (z==0) fprintf(out,"Case #%d: Volunteer cheated!\n",i);
		else if (z==1) fprintf(out,"Case #%d: %d\n",i,d);
		else fprintf(out,"Case #%d: Bad magician!\n",i);
	}
	fclose(in);
	fclose(out);
	return 0;
}
