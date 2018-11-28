#include <cstdio>

int main()
{
	//ifstream cin("A-small-attempt0.in");
	//ofstream cout("output.txt");
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int number, counter;
	double C, F, X;
	double sec, cook;
	double noFarm, farm, buildFarm;
	double income;
	scanf("%d", &number);
	for(counter=1; counter <= number; counter++)
	{
		income = 2.0;
		sec = 0.0;
		cook = 0.0;
		scanf("%lf%lf%lf", &C, &F, &X);
		while(cook < X)
		{
			noFarm = X / income;
			buildFarm = C / income;
			farm = buildFarm + ( X / (F + income) );
			if(noFarm < farm)
			{
				sec += noFarm;
				cook = X;
			}
			else
			{
				sec += buildFarm;
				income += F;
			}
		}
		printf("Case #%d: %.7lf\n", counter, sec);
	}
	return 0;
}