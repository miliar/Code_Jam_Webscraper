#include <stdio.h>

int main()
{
	int n,i;
	double pes=2.0,C,F,X,sec=0.0;

	FILE *fs = fopen("B-small-attempt0.in","rt");
	FILE *fp = fopen("output.out","wt");
	fscanf(fs,"%d",&n);

	for(i=0;i<n;i++)
	{
		fscanf(fs,"%lf %lf %lf",&C,&F,&X);

		sec=0.0;
		pes=2.0;

		while(1)
		{
			if(X/(pes+F)+C/pes>=X/pes)
			{
				sec+=X/pes;
				break;
			}
			sec+=C/pes;
			pes+=F;
		}
		fprintf(fp,"Case #%d: %.7lf\n",i+1,sec);
	}
	fclose(fs);
	fclose(fp);
	return 0;
}