#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <math.h>


int main(){
	double T,C,F,X,answer=0,cookie=2;
	int i,j;
	int turn=1;


	FILE *input;
	FILE *output;

	input=fopen("B-large.in","r");
	output=fopen("output.txt","w");

	fscanf(input,"%lf\n",&T);

	for(i=0;i<T;i++){
		fscanf(input,"%lf %lf %lf\n",&C,&F,&X);

		
		while(1){
			if(X/(F+cookie)<(X-C)/cookie){
				answer+=C/cookie;
				cookie+=F;
			}
			else{
				answer+=X/cookie;
				break;
			}
		}

		fprintf(output,"Case #%d: %0.7lf\n",turn,answer);

		turn++;
		answer=0;
		cookie=2;
	}

	fclose(input);
	fclose(output);

	return 0;
}

