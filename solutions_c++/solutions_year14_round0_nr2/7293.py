#include <iostream>
#include <iomanip>

using namespace std;

double find_opttime(double C, double F, double X, double orig)
{
	double results = 0;

	while(X/orig > X/(orig + F) + C/orig)
	{
		results += C/orig;
		orig += F;
	}
	return results + X/orig;
}

int main()
{
	int testcases;
	cin >> testcases;

	for(int i = 0; i < testcases; i++)
	{
		double C, F, X;
		cin >> C >> F >> X;
		cout << "Case #" << i + 1 << ": " << fixed << setprecision(7) << find_opttime(C, F, X, 2.00) << endl;
	}
}