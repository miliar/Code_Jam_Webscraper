#include <stdio.h>

int main(){

	FILE* fp1=fopen("B-Large.in","r");
	FILE* fp2=fopen("B-Large-attempt0.out","w");

	int T;
	int cas=1;
	fscanf(fp1,"%d",&T);
	while(T--){
		long double c,f,x;

		long double cook=0;
		long double cospeed=2;
		long double b1;
		long double b2;

		long double sum=0;
		fscanf(fp1,"%Lf%Lf%Lf",&c,&f,&x);
		while(1){
			b1=c/cospeed;
			b1+=x/(cospeed+f);
			b2=x/cospeed;
			if(b1>b2)
				break;
			sum+=c/cospeed;
			cospeed+=f;
		}
		sum+=x/cospeed;
		fprintf(fp2,"Case #%d: %.7Lf\n",cas++,sum);
	}
	
	fclose(fp1);
	fclose(fp2);
	return 0;
}