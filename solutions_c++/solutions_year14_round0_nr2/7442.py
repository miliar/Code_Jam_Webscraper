#include <stdio.h>
#include <stdlib.h>

using namespace std; 

int cnt=0;

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	while(t--){
		double C, F, X, K=2.0, res=0.0;
		scanf("%lf%lf%lf", &C, &F, &X);
		while(X/K > C/K + (X/(K+F))){
			res += C/K;
			K += F;	
			//printf("---%lf\n", res);
		}
		res += X/K; 
		printf("Case #%d: %lf\n", ++cnt, res);
	}
	return 0;
}
