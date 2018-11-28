#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <climits>
#include <cmath>

using namespace std;

double calculate_time(int rate, double end, double cost, double extra_rate)
{
	double time1, time2, time_cost;

	time1 = end/rate;
	time1 = time1*10000000000;
	if (cost <= end) {
		time_cost = cost/rate;
		time_cost = time_cost*10000000000;
		time2 = end/(rate + extra_rate);
		time2 = time2*10000000000;
		if (time1 <= time2 + time_cost)
			return time1;
		else
			return time_cost + calculate_time(rate+extra_rate, end, cost, extra_rate);
	}
	return time1;
}

int main(int argc, const char *argv[])
{
	int caseNr;
	int caseId;
	scanf("%d", &caseNr);
	for (caseId=0; caseId<caseNr; caseId++) {
		double c,f,x;
		double time;

		scanf("%lf", &c);
		scanf("%lf", &f);
		scanf("%lf", &x);
		//time = calculate_time(2*100000, round((double)(int)(x*100000)), round((double)(int)(c*100000)), round((double)(int)(f*100000)));
		time = calculate_time(2*100000, round(x*100000), round(c*100000), round(f*100000));
		printf("Case #%d: %.7f\n", caseId+1, time/10000000000);
	}
	return 0;
}
