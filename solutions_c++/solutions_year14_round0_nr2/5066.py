#include "stdio.h"
#include "string.h"


int main(){
	int t;
	double C,F,X;
	double tmp;
	double now;
	double ans;

	FILE *fp;
	FILE *fp2;

	fp=fopen("B-large.in","r");
	fp2=fopen("result.txt","w");
	fscanf(fp,"%d",&t);

	for(int i=0;i<t;i++){
		now=2.0;
		tmp=0.0;
		fscanf(fp,"%lf %lf %lf",&C,&F,&X);
		while(1){
			if(X/now<C/now+X/(now+F)){
				break;
			}
			tmp+=C/now;
			now+=F;
		}
		ans=tmp+X/now;
		fprintf(fp2,"Case #%d: %.7lf\n",i+1,ans);
	}

	fclose(fp);
	fclose(fp2);

	return 0;
}