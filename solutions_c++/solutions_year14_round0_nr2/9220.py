
#include <cstdio>

int N;
double C;
double F;
double X;

void f(int number){
	double prev_t = 100000000;
	double t = 0;
	long n = 0;
	while(1){
		t = 0;
		t += X/(2+n*F);
		double r = 0;
		for(int i = 0;i < n;i++){
			r += 1/(2+i*F);
		}
		r *= C;
		t += r;
		n += 1;
		if(t > prev_t){
			break;
		}
		prev_t = t;
	}
	printf("Case #%d: %lf\n",number,prev_t);
}

int main(){
	scanf("%d\n",&N);
	for(int i = 0;i < N;i++){
		scanf("%lf %lf %lf",&C,&F,&X);
		f(i+1);
	}
}
