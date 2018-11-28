#include <stdio.h>
int t;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int k;
	scanf("%d",&t);
	for(k=1;k<=t;k++){
		double rate=2.0,time=0.0,c,f,x;
		printf("Case #%d: ",k);
		scanf("%lf %lf %lf",&c,&f,&x);
		while(1){
			if(c/rate+x/(rate+f)<x/rate){
				time+=c/rate;
				rate+=f;
			}
			else{
				time+=x/rate;
				break;
			}
		}
		printf("%lf\n",time);
	}
	return 0;
}