#include <stdio.h>

int T;
double c,f,x, minTime;

int main() {
	double prod, cookie, time;
	scanf("%d",&T);
	for (int Cas=1;Cas<=T;++Cas) {
		scanf("%lf%lf%lf", &c,&f,&x);
		prod=2, cookie=0, time=0;

		minTime=x/prod;
		while (true) {
			double wait=c/prod;
			time+=wait;
			prod+=f;
			if (time+x/prod>minTime)
				break;
			minTime=time+x/prod;
		}
		printf("Case #%d: %.8lf\n", Cas, minTime);
	}
	return 0;
}
