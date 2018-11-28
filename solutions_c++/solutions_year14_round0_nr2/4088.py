#include<stdio.h>
#include<time.h>

#define EPS 0.0000001

int main(){
	int n=1, input;
	scanf("%d", &input);
	long double c, x, f;
	while(n<=input){
		long double rate=2, t=0;
		scanf("%Lf%Lf%Lf", &c, &f, &x);
	while(1){
		if(x/rate < c/rate + x/(rate+f)){
			t+=x/rate;
			break;
		}
			t+=c/rate;
			rate+=f;
		}
		printf("Case #%d%s%Lf", n, ": ", t);
		n++;
		printf("\n"); 
	}
	return 0;
}