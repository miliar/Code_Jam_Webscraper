#include <stdio.h>
#define row 4
#define col 4
int main(){
	FILE *f;
	f=fopen("answer.txt","w");
	int z;
	int k=1;
	double C,F,X,a,b;
	double CF;
	double time;
	scanf("%d",&z);
	while(k<=z){
		CF=2.0;time=0.0;
		scanf("%lf %lf %lf",&C,&F,&X);
		while(1){
			a=C/CF+X/(CF+F);
			b=X/CF;
			if(a<b){
				time+=C/CF;
				CF+=F;
			}
			if(a>=b){
				time+=X/CF;
				break;
			}
		}
		fprintf(f,"Case #%d: ",k++);
		fprintf(f,"%lf\n",time);
	}
	fclose(f);
}