#include<iostream>
#include<cstdio>
using namespace std;

int main(){
	double F,X,C,currRate,time,numCookie;
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		currRate=2;
		time=0;
		numCookie=0;
		scanf("%lf",&C);
		scanf("%lf",&F);
		scanf("%lf",&X);
		while(numCookie<X){
			numCookie=C;
			time+=C/currRate;
			if(X/(F+currRate)<(X-C)/currRate) {
				currRate+=F;
				numCookie=0;
			}
			else{
				time+=(X-C)/currRate;
				numCookie=X;
			}
		}
		printf("Case #%d: %.7f\n",t+1,time);
	}

}
