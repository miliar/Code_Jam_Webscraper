#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	double c,f,x;
	int test=0,count;
	FILE *fin=fopen("in.txt","r");
	FILE *fout=fopen("out.txt","w");
	fscanf(fin,"%d",&count);
	while(count--)
	{
		test++;
		fscanf(fin,"%lf %lf %lf",&c,&f,&x);
		double speed=2.0,tme=0.0;
		while((x/speed)>(c/speed+x/(speed+f)))
		{

			tme+=(c/speed);
			speed+=f;
		}
		tme+=(x/speed);
		fprintf(fout,"Case #%d: %.7lf\n",test,tme);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}