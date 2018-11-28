#include<stdio.h>

long double C, F, X, rate = 2.0,time;

void evaluate(){
	time = X/rate;
	long double  timeToGenerateFarm, timeToGenerateCookies, prevTime = 0.0;
	while(1){
		timeToGenerateFarm = C/rate;rate = rate + F;
		timeToGenerateCookies = X/rate;
		prevTime += timeToGenerateFarm;
		if(prevTime + timeToGenerateCookies < time){
			time = prevTime + timeToGenerateCookies;
		}else break; 
	} 
}

int main(){
	freopen("abc.txt","w",stdout);
	freopen("pqr.txt","r",stdin);
	int T,casee = 1;
	scanf("%d",&T);
	while(T--){
		scanf("%Lf %Lf %Lf",&C, &F, &X);
		//printf("%Lf %Lf %Lf\n",C, F, X);
		evaluate();
		printf("Case #%d: %Lf\n",casee,time);
		rate = 2.0;
		casee++;
	}
	fclose(stdin);
	fclose(stdout);
return 0;
}
/*
4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0
*/

