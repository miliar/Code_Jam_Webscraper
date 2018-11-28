#include <limits>
#include <iomanip>
#include <iostream>

using namespace std;

typedef std::numeric_limits< double > dbl;

double computeTime(double C, double F, double X)
{
	double newTime = X / 2.0f;
	double prevTime = 1 + X / 2.0f;
	double sumofpt = 0;
	long i = 0, j;

	for(i = 0, j = 1; newTime < prevTime; i++, j++)
	{
		prevTime = newTime;
		sumofpt += C / (2 + i * F);
		newTime = sumofpt + (X / (2 + j * F));
	} 

	return prevTime;
}

int main()
{
	int t, T;

	cin >> T;

	for(t = 0; t < T; t++)
	{
		double C, F, X;

		cin >> C >> F >> X;
		
		cout << "Case #" << t+1 << ": " << fixed << setprecision(7) << computeTime(C, F, X) << endl;
	}
}
