#include <stdio.h>
#include <stdlib.h>
#include <math.h>




void main(void){

	FILE *fp,*fp2;
	int times;
	int i=0;
	int j,k;
	double second;
	double cookies;
	long double bestTime;
	double increment;




	float C,F,X;



	char *message_1 = "Bad magician!";
	char *message_2 = "Volunteer cheated!";

	fp = fopen("B-small-attempt0.in","r");
	fp2 = fopen("test.out","w");
	if(!fp){
		printf("error.");
		return;
	}
	if(!fp2){
		printf("error.");
		return;
	}

	fscanf(fp,"%d", &times);
	i=1;
	while(times--){
	
		if(feof(fp)){
				break;
		}
		second=0;
		cookies=0;
		
		
		fscanf(fp,"%f %f %f", &C,&F, &X);
		bestTime = X/2.0;	
	

		for(j=1;j<50000;j++){
		long double temp =0;
			for(k=0;k<j;k++){
				temp+=C/(2.0+F*k);				
			}
			temp+=X/(2.0+F*k);		

			if(bestTime<temp){
				printf("Case #%d: %.10lf\n",i, bestTime);
				fprintf(fp2,"Case #%d: %.10lf\n",i, bestTime);
				break;
			}
			else{
				bestTime=temp;
				
			}
		}
		
		
		i++;
		
	}
	
	fclose(fp);

	fclose(fp2);

}