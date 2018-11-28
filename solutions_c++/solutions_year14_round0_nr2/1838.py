#include"stdio.h"
int main(){
	int n,i;
	double C,F,X,T=0,t,p,g=0;
	scanf("%d",&n);
	for(i=1;i<=n;i++){
		T=0;p=2;g=0;//initialize
		scanf("%lf %lf %lf",&C,&F,&X);
		if(C>=X){
			T=(X-g)/p;
		}
		else while(1)
			if(g>=C){//g==C
				t=(X-(g-C))/(p+F);
				if((X-g)/p>t){
					p+=F;
					g-=C;
				}
				else{
					T+=(X-g)/p;
					break;
				}
			}
			else{//g==0
				g+=C;
				T+=C/p;
			}
		printf("Case #%d: %.7f\n",i,T);
	}
}