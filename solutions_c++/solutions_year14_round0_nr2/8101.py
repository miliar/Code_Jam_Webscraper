#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>

using namespace std;

int main()
{

int T=0,Tcount=0;
scanf("%d\n",&T);
for(Tcount=1;Tcount<=T;Tcount++)
{
	double X=0;	//Target cookie	
	double F=0;	//Increment Rate
	double C=0;	//Time to buy cookie
	
	double Tbase=0;	//Max time limit
	double time=0;
	int I=0;
	int J=0;
	double farmtime=0.0;
	
	scanf("%lf %lf %lf\n",&C,&F,&X);
	Tbase=X/2.0;
	
	for(I=1;time<=Tbase;I++)
	{
		farmtime=0.0;
		for(J=0;J<I;J++)
		{
		farmtime=farmtime+(C/(2.0+J*F));
		}
		
		time=(X/(2.0+I*F))+farmtime;
		if(time<Tbase)
		{
		Tbase=time;
		}
	}
	printf("Case #%d: %.7lf\n",Tcount,Tbase);
	
	
}
	

return 0;
}
