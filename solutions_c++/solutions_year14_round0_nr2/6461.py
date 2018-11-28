#include <iostream>
#include<cstdio>
using namespace std;

int main() {
	int t,T;
	double c,f,x,current,numFarms,timeElapsed,minTime;
	double timeTillNextFarm;
	double timeTillWin;
	scanf("%d",&T);
	for(t=1;t<=T;++t){
		scanf("%lf %lf %lf",&c,&f,&x);
		//c-farm cost
		//f-farm cps
		//x-current
		//gain 2 cps normal.
		current=0;
		numFarms=0;
		timeElapsed=0;
		minTime=x/2;
		while(current<x){
			timeTillNextFarm=((double)c/(numFarms*f+2));
			current+=timeTillNextFarm;
			++numFarms;
			timeTillWin=x/(numFarms*f+2);
			if(current+timeTillWin<minTime)
				minTime=timeTillWin+current;
			else break;

		}
		printf("Case #%d: %4.7lf\n",t,minTime);

	}
	return 0;
}
