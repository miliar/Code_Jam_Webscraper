#include <cstdio>

int nFarm;
double C, F, X;
double Y;
double cur;

double rate(int n){
	return 2.0+n*F;
}

double getTime(int n){
	if(X/rate(n) < C/rate(n) + X/rate(n+1)){
		return X/rate(n);
	}
	return C/rate(n)+getTime(n+1);
}

double getTime2(){
	double cur=0;
	int n=0;
	int get=0;
	while(!get){
		//printf("%d %lf %lf %lf\n",n, rate(n), cur+X/rate(n), cur+C/rate(n) + X/rate(n+1));
		if(X/rate(n) < C/rate(n) + X/rate(n+1)){
			cur+=X/rate(n);
			get = 1;
		}else{
			cur+=C/rate(n);
			n++;
			
		}
	}
	//printf("n=%d\n",n);
	return cur;
}

int main(){
	int T, cases=1;
	scanf("%d\n",&T);
	
	
	while(T--){
		scanf("%lf %lf %lf\n", &C, &F, &X);
		Y=getTime2();
		
		printf("Case #%d: %.7lf\n", cases++, Y);
	}
	return 0;
}

