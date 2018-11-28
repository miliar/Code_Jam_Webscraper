#include <stdio.h>


void solution(FILE* finput,FILE* foutput,int countofcase)
{
	double price;
	double addspeed;
	double finalscore;
	fscanf(finput,"%lf",&price);
	fscanf(finput,"%lf",&addspeed);
	fscanf(finput,"%lf",&finalscore);
	//printf("%lf %lf %lf",price,addspeed,finalscore);
	//printf("%d\n",52/4);
	double sumoftime=0;
	double speed=2.0;
	while((price/speed+finalscore/(speed+addspeed))<(finalscore/speed))
	{
		sumoftime+=price/speed;
		speed+=addspeed;
	}

	sumoftime+=finalscore/speed;
	fprintf(foutput,"Case #%d: %lf\n",countofcase+1,sumoftime);
}


void main()
{
	FILE *finput=fopen("B-large.in","r");
	FILE *foutput=fopen("B-large_output.txt","w");

	int numofcase;

	fscanf(finput,"%d",&numofcase);
	for (int i=0;i<numofcase;i++)
	{
		solution(finput,foutput,i);
	}


	fclose(finput);
	fclose(foutput);
}