#include <stdio.h>
#include <stdlib.h>

int main(){
	int t;
	scanf("%d",&t);
	double sol[t];
	for(int i=0;i<t;i++){
		double C,F,X;
		scanf("%lf %lf %lf",&C,&F,&X);
		double TIME=0, V=2;
		while (1){
			if( ((X-C)/V) <= (X/(V+F)) ){
				TIME += X/V;
				break;
			}else{
				TIME += C/V;
				V+=F;
			}
		}
		sol[i]=TIME;
	}
	for(int i=0;i<t;i++)
		printf("Case #%d: %.7lf\n",i+1,sol[i]);
}
