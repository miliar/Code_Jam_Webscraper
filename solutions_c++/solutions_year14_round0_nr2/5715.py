#include<stdio.h>
int T;
double C,F,X;
double cps=2.0,ans;



int main(){
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		printf("Case #%d: ",i+1);
		scanf("%lf %lf %lf",&C,&F,&X);
		while(1){
			double ft1=X/cps;
			double ft2=C/cps+X/(cps+F);
			if(ft1<ft2){
				ans+=ft1;
				break;
			}
			else{
				ans+=C/cps;
				cps+=F;
			}
		}
		printf("%lf\n",ans);
		ans=0;
		cps=2.0;
	}
	return 0;
}