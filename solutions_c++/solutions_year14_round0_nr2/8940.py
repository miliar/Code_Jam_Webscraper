#include <stdio.h>
#include <stdlib.h>
#include<iostream>
#include<iomanip>

using namespace std;

FILE *inp;
//FILE *out;

int cases;
double C,F,X;

int main(){
	int i;
	
	//opening data file and storing No of cases
	//B-small-attempt0.in
	{
    	inp = fopen("B-large.in","rb");
    //	out = fopen("out.txt","w");
//<input.txt >output.txt
    	fscanf(inp, "%d\n", &cases);
	}
	
	for(i=0;i<cases;i++){
		
		double time=0;
		double speed = 2;
		
		fscanf(inp, "%lf %lf %lf\n", &C, &F, &X);
		//printf("c=%lf, f=%lf, x=%lf\n",C,F,X);
		
		while((X-C)/speed>X/(speed+F)){
			time = time + C/speed;
			speed = speed + F;
		}
		time = time + X/speed;
		//fprintf(out, "Case #%d: %lf\n",(i+1),time);
		cout<<"Case #"<<i+1<<": "<<setprecision(7)<<fixed<<time<<endl;;
	}
	
	fclose(inp);
	//fclose(out);
	
	return 0;
}
