#include<cstdio>

int main(){
	int testcase,tc;
	double curRate;
	double farmCost;
	double addition;
	double goal;
	double time;
	double wastedTime;

	scanf("%d",&testcase);
	for(tc=1;tc<=testcase;tc++){
		scanf("%lf %lf %lf",&farmCost,&addition,&goal);

		curRate = 2;
		wastedTime = 0;
		do{
			time = wastedTime + goal/curRate;

			wastedTime += farmCost/curRate;
			curRate += addition;
		}while(wastedTime + goal/curRate < time + 0.0000005);

		printf("Case #%d: %lf\n",tc,time);
	}

	return 0;
}
