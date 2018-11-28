#include <stdio.h>

int main()
{
	int T;

	scanf("%d", &T);

	for(int i=1; i<=T; i++) {

		double time = 0.0, farmCost, goal;
		double countPerSec = 2.0, countFromFarm;

		scanf("%lf %lf %lf", &farmCost, &countFromFarm, &goal);

		while(true) {
			// 농장 안살때
			double time1 = time + goal / countPerSec;

			// 농장을 살 때
			double time2 = time + (farmCost / countPerSec) + goal / (countPerSec + countFromFarm);

			// 농장을 사는 것이 이득일때
			if (time1 > time2) {
				time += farmCost / countPerSec;
				countPerSec += countFromFarm;
			} else {
				time = time1;
				break ;
			}
		}

		printf("Case #%d: %.7lf\n", i, time);
	}
}
