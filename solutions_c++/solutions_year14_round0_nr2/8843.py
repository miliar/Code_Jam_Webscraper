#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<string.h>
#include<fstream>
#include<limits.h>
int main()
{
	FILE *f,*fp;
	f=fopen("D:\B-large.in","r");
	fp=fopen("D:\kaiwon.in","w");
	int n=1,T;
	fscanf(f,"%d",&T);
	while(T--)
	{
		double C,F,X,q=2.0,time=0.0,time1=0.0,time2=0.0;
		fscanf(f,"%lf %lf %lf",&C,&F,&X);
		time1=(X/q);
		time=time+(C/q);
		time2=time+(X/(F+q));		
		while(time1>time2)
		{
			q=q+F;
			time1=time2;
			time+=(C/q);
			time2=time+(X/(F+q));
		}
		fprintf(fp,"Case #%d: %f\n",n++,time1);
	}
	fclose(f);
	fclose(fp);
	return 0;
}
