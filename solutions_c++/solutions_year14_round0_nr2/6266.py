#include "stdio.h"
#include "stdlib.h"

int main(){
	FILE *ptr,*optr;
	ptr=fopen("B-large.in","r");
	optr=fopen("output.out","w");
	long double C,F,X;
	long double init_rate=2;
	 
	long double times=0;
	int test_run;
	fscanf(ptr,"%d",&test_run);

	for(int run=0; run<test_run; run++){
		fscanf(ptr,"%lf%lf%lf",&C,&F,&X);
		times=(X)/init_rate;
		
		for(int far_num=1; far_num<100000; far_num++){
			long double times_tmp;
			long double sum=0;
			for(int i=0;i<far_num;i++){
				sum=sum+(C)/(init_rate+i*F);
			}
			times_tmp=sum+(X)/(init_rate+far_num*F);
			
			if(times_tmp<times){
				times=times_tmp;
			}
			else{
				break;
			}
			
			
		}
		fprintf(optr,"Case #%d: %.7lf\n",run+1,times);

		

	}
	fclose(ptr);
	fclose(optr);




	return 0;
}