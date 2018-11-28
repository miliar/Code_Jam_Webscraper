#include<stdio.h>
int main(){
	int N;
	while(~scanf("%d",&N))
		for(int z=1;z<=N;z++){
			double C,F,X;
			scanf("%lf%lf%lf",&C,&F,&X);
			double farmtime[100000],rate[100000];
			rate[0]=2.0;
			farmtime[0]=0.0;
			farmtime[1]=C/rate[0];
			for(int i=1;i<100000;i++){
				rate[i]=rate[i-1]+F;
				farmtime[i]=C/rate[i-1]+farmtime[i-1];
			}
			printf("Case #%d: ",z);
			for(int i=0;i<100000;i++)
				if(X/rate[i]+farmtime[i]<X/rate[i+1]+farmtime[i+1]){
					printf("%.7lf\n",X/rate[i]+farmtime[i]);
					break;
				}
		}
	return 0;
}