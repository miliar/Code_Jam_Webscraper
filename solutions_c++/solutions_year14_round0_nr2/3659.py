#include <iostream>
#include<stdio.h>
using namespace std;

int main() 
{
	int t;
	double c,f,x,rate,time;
	int i;
	FILE *ifp, *ofp;
	char outputFilename[] = "CookieClickerAlphaOutput.txt";
	
	ifp = fopen("B-large.in", "r");
	ofp = fopen(outputFilename, "w");
	
	fscanf(ifp,"%d", &t);
	for(i=1;i<=t;i++)
	{
		fscanf(ifp,"%lf",&c);
		fscanf(ifp,"%lf",&f);
		fscanf(ifp,"%lf",&x);
		rate=2.0;time=0.0;
		while(1)
		{
			if((x/rate) <= ((c/rate) + (x/(rate+f))))
			{
				time+=x/rate;
				break;
			}
			else
			{
				time+=c/rate;
				rate+=f;
			}
		}
		fprintf(ofp,"Case #%d: %.7lf",i,time);
		if(i!=t)
		   fprintf(ofp,"\n");
		//   printf("%0.5lf %0.5lf %0.5lf \n",c,f,x);
	}
	return 0;
}
