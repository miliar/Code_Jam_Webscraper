#include <stdio.h>
#include <stdlib.h>
#include <string.h>
double calcTime(int step,double c,double x,double f)
{//step>=2
	double totalTime = c/2.0;
	for(int i=1;i<step-1;++i)
	{
		totalTime+= c/(2.0+i*1.0*f);
	}
	totalTime+=x/(2.0+(step-1)*1.0*f);
	return totalTime;
}
int main()
{
	FILE *f,*fout;
	f = fopen("inb.txt","r");
	fout = fopen("outb.txt","w+");
	char c[1024];
	int n;
	fscanf(f,"%d",&n);
	for(int i=0;i<n;++i)
	{
		double X,C,F;
		fscanf(f,"%lf %lf %lf",&C,&F,&X);
		double step = 0;
		double val1 = X/2.0;
		double val2 = 0.0;
		step = X/C-2.0/F+1.0;
		if(step>0.000001)
		{
			int times1, times2;
			times1 = (int)step;
			times2 = 1+(int)step;
			if(times1>=2)
			{
				val2 = calcTime(times1,C,X,F);
				double val3 = calcTime(times2,C,X,F);
				val2 = val2>val3?val3:val2;
				val1 = val1>val2?val2:val1;
			}
			else
			{
				if(times2>=2)
				{
					val2 = calcTime(times2,C,X,F);
					val1 = val1>val2?val2:val1;
				}
			}
		}
		fprintf(fout,"Case #%d: %.7lf\n",i+1,val1);
	}
	fclose(f);
	return 1;
}