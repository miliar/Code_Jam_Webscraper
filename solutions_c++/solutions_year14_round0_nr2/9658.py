#include <cstdio>
double findout(double c, double f, double x)
{
	double inc = 2;
	double spentOnFarm = 0, spentOnWin = x / inc;
	double min = spentOnWin;
	for (int i = 0; i < 10001; i++)
	{
		spentOnFarm += c / inc;
		inc += f;
		spentOnWin = spentOnFarm + x / inc;
		min = (spentOnWin < min ? spentOnWin : min);
	}
	return min;
}
int main(int argc, char* argv[])
{
	if (argc > 1)
		freopen(argv[1], "r", stdin);
	int t;
	double c, f, x;
	double sec;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++)
	{
		scanf("%lf%lf%lf", &c, &f, &x);
		sec = findout(c, f, x);
		printf("Case #%d: %.7lf\n", cas, sec);
	}
	return 0;
}