#include<stdio.h>
int main(void){
	FILE *f1,*f2;
	f1=fopen("B-large.in","r");
	f2=fopen("output.txt","w");
	int t,tc;
	double c,f,x,cps;
	double total_s,predict,farm_p;
	
	fscanf(f1,"%d",&t);

	for(tc=1;tc<=t;tc++){
		fscanf(f1,"%lf %lf %lf",&c,&f,&x); 
		cps=2.0;
		total_s=0;
		predict=0;
		farm_p=0;

		for(;;){
			predict=x/cps;
			farm_p=c/cps + x/(cps+f);
			if(predict<=farm_p){
				fprintf(f2,"Case #%d: %.7lf\n",tc,predict+total_s);
				break;
			}
			total_s+=c/cps;
			cps+=f;					
		}
	}
	return 0;
}