#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <limits.h>

using namespace std;

FILE *in, *out;


int main(){

	int t=0;
	int i=0, j=0;
	long double c,f,x;
	long double persec, forfarm,time, keep;



	in=fopen("B-large.in","r");
	out=fopen("B-large.out","w");

//	in=fopen("input.txt","r");
//	out=fopen("output.txt","w");



	fscanf(in,"%d",&t);


	for(int a=0; a<t; a++){
		persec=2;
		time=0;

		fscanf(in,"%lf %lf %lf",&c,&f,&x);
		
		
		while(1){                              //large케이스는 개선필요??
			keep=x/persec;

			forfarm=(c/persec)+(x/(persec+f));

			if(keep<forfarm){   
				time+=keep;
				break;
			}

			time+=c/persec;
			persec+=f;
			
		}
		
		fprintf(out,"Case #%d: %lf\r\n",a+1,time);

	}

	fclose(in);
	fclose(out);

	return 0;


}