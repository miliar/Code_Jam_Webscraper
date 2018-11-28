#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE *in,*out;
	in = fopen("D-small-attempt0.in","r");
	out = fopen("dsmall.out","w");
	int x,r,c,z,t,layer;
	fscanf(in,"%d",&t);
	for (layer=1; layer<=t; layer++)
	{
		fscanf(in,"%d%d%d",&x,&r,&c);
		if (x==1) fprintf(out,"Case #%d: GABRIEL\n",layer);
		if (x==2)
		{
			if (r*c%x==0) 
				fprintf(out,"Case #%d: GABRIEL\n",layer);
			else
				fprintf(out,"Case #%d: RICHARD\n",layer);
		}
		if (x==3)
		{
			if ((r*c%x==0)&&(r>1)&&(c>1))
				fprintf(out,"Case #%d: GABRIEL\n",layer);
			else
				fprintf(out,"Case #%d: RICHARD\n",layer);
		}
		if (x==4)
		{
			if (r<c)
			{
				z = r; r = c; c = z;
			}
			if ((r==4)&&(c>=3)) 
				fprintf(out,"Case #%d: GABRIEL\n",layer);
			else 
				fprintf(out,"Case #%d: RICHARD\n",layer);
		}
	}
	fclose(in);
	fclose(out);
	return 0;
}
