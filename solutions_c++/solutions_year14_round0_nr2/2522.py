#include<stdio.h>
FILE *in=fopen("1.in","r");
FILE *out=fopen("1.out","w");
int TT,Tcnt;
double C,F,X,m;
double Cf=2,Time,Min;
int main()
{
	fscanf(in,"%d",&TT);
	for(Tcnt=1;Tcnt<=TT;Tcnt++)
	{
		fscanf(in,"%lf %lf %lf",&C,&F,&X);
		Cf=2;
		Time=0;
		Min=X/Cf;

        
		while(1)
		{
			Time+=C/Cf;
			Cf+=F;
			if(Min>Time+X/Cf)Min=Time+X/Cf;
			else break;
		}
		fprintf(out,"Case #%d: %.7lf\n",Tcnt,Min);
	}
	return 0;
}