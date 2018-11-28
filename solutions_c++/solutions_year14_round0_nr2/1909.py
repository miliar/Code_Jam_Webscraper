#include "stdio.h"
#include "iostream"


int main()
{
	FILE * finp;
	FILE * foutp;

	int t;
	double rs,c,f,x,rate;

	if((finp=fopen("A-small-attempt0.in","r"))==NULL)
	{
		printf("error");
		exit(0);
	}
	if((foutp=fopen("A-small-attempt0.out","w"))==NULL)
	{
		printf("error");
		exit(0);
	}

	fscanf(finp,"%d",&t);

	for(int i=0;i<t;i++)
	{
		fscanf(finp,"%lf%lf%lf",&c,&f,&x);
		rate=2.0;rs=0.0;
		while((x/rate)>(x/(rate+f)+c/rate))
		{
			rs+=c/rate;
			rate+=f;
		}
		rs+=x/rate;

		fprintf(foutp,"Case #%d: %lf\n",i+1,rs);
	}

	fclose(finp);
	fclose(foutp);

	return 0;
}
