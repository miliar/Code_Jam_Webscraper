#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

void solve();

int main(){
	int cases;
	scanf("%d", &cases);
	for(int i=0; i<cases; i++){
		printf("Case #%d: ", (i+1));
		solve();
	}
	return 0;
}

void solve(){
	double C, F, X, time = 0.0, rate = 2.0, newtime;
	scanf("%lf %lf %lf", &C, &F, &X);

	double best = X/rate;

	while(1){
		time = time + (C/rate);
		rate += F;
		newtime = time + (X/rate);
		if(newtime<best){
			best = newtime;
		}else{
			break;
		}
	}
	printf("%.7lf\n", best);
}