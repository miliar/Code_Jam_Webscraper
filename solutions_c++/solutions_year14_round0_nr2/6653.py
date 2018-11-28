#include "iostream"
#include "cmath"

using namespace std;

double fun(double C, double F, double X)
{
	double result, rate, time;
	time = 0;
	rate = 2;
	result = X / rate;

	while (time + X/rate <= result)
	{
		result = time + X / rate;
		time += C / rate;
		rate += F;
	}
	return result;
}


int main()
{
	double C, F, X, result;
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		cin >> C >> F >> X;
		result = fun(C, F, X);
		printf("Case #%d: %.7f\n", i, result);
		//cout << "Case #" << i << ": " << result << endl;
	}

	//system("pause");
	return 0;
}