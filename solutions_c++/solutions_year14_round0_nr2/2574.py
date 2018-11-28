#include <cstdio>
#include <algorithm>

const double PRECISION = 0.0000001;
int t;
double c,f,x,solution,currProduction,timeForBuild;

inline double calcTime()
{
	return timeForBuild + x/currProduction;
}

int main()
{
	scanf("%d", &t);
	for(int test = 1; test <= t; ++test)
	{
		currProduction = 2.0;
		timeForBuild = 0.0;
		scanf("%lf%lf%lf", &c, &f, &x);
		solution = x/currProduction;

		while((solution-timeForBuild) > PRECISION)
		{
			solution = std::min(solution,calcTime());
			timeForBuild += c/currProduction;
			currProduction += f;
		}

		printf("Case #%d: %.7lf\n", test, solution);
	}
}
