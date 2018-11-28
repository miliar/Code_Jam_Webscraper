#include<algorithm>
#include<cstdio>
#include<iostream> 
using namespace std;
double countTime(double c, double f, double x)
{
	double result = 0.0;
	double optFirst, OptFirstCon, optFirstSum, optSecond;
	double b_f = 2.0;
	// 1 - buy farm, 2 - buy cookies!
	int option = -1;
	while (true)
	{
		if (c > x)
		{
			result += x / b_f;
			break;
		} else
		{
			//buy farm
			optFirst = c / b_f;
			//buy cookies
			optSecond = x / b_f;
			// buy farm + buy cookies
			OptFirstCon = x / (b_f + f);
			optFirstSum = optFirst + OptFirstCon;

			if (optFirstSum < optSecond)
			{
				result += optFirst;
				b_f += f;
			}
			else
			{
				result += optSecond;
				break;
			}
		}
	}
	return result;
}
int main()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);
		printf("Case #%d: ", i + 1);
		printf("%.7lf\n", countTime(c, f, x));

	}
	return 0;
}