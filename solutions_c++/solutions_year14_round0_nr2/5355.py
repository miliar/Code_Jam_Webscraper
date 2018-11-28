#include <iostream>
#include <cstdio>

double solve(double C, double F, double X)
{
	double t_bs = 0;
	double prev = 0;

	for(int i = 0; ; i++)
	{
		double t_f = X / (i*F + 2);

		double curr = t_bs + t_f;
		if(i && (curr > prev))
			return prev;
		prev = curr;
		t_bs += C / (i*F + 2);
	}
}

int main()
{
	int count;
	std::cin >> count;
	for(int i = 1; i <= count; i++)
	{
		double c,f,x;
		std::cin >> c >> f >> x;
		double res = solve(c,f,x);
		printf("Case #%d: %.7f\n", i, res);
	}
}
