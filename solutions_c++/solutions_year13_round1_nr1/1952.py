#include <stdio.h>
#include <math.h>
int T;
long long r,t;
int main(){
	
	scanf("%d",&T);
	for(int iii=0;iii<T;iii++){

		scanf("%lld %lld",&r,&t);


		double n=(-3-2*r+sqrt((double)((double)(3+2*r)*(double)(3+2*r)+8*t)))/4.0;
		n-=2;
		n=(long long)n;

		while(2*n*n+3*n+2*n*r+2*(double)r+1<=t){
			n++;	
		}
		//printf("%lf\n",2*n*n+3*n+2*n*r+2*(double)r+1);
		printf("Case #%d: %lld\n",iii+1,(long long)n);


	}

	
}