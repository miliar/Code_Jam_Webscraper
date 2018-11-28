#include <cstdio>

int t;
double c, f, x;

double deal()
{
	if (c >= x) return x/2.0;
	double min = x/2.0;
	int time = 1;
	double wait = 0;
	while (true) {
		wait += c / (2.0 + f * (time-1));
		double res = wait + x / (2.0 + f * time);
		if (res < min) min = res;
		else break;
		++time;
	}
	return min;
}

int main()
{
	scanf("%d",&t);
	for (int cas=1; cas<=t; ++cas) {
		scanf("%lf%lf%lf",&c,&f,&x);
		printf("Case #%d: %.7lf\n",cas,deal());
	}
	return 0;
}
