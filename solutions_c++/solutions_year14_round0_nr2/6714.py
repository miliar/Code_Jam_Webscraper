#include <iostream>
#include <limits>
#include <iomanip>

using namespace std;

double prob02(double C, double F, double X)
{
	// calc first intersection with X
	double b = 0;
	double rate = 2.0;

	double t1 = X/rate;
	double t2 = numeric_limits<double>::infinity();

	while(t1 < t2)
	{
		t2 = t1;

		double tC = (C-b)/rate;

		rate += F;
		b = -rate * tC;

		t1 = (X-b)/rate;
	}

	return t2;
}

int main(int argc, char **argv)
{

	int T;
	cin >> T;

	for(int i=0; i < T; ++i)
	{
		double C,F,X;

		cin >> C;
		cin >> F;
		cin >> X;

		cout << "Case #" << fixed << setprecision(7) << i+1 << ": " << prob02(C,F,X) << endl;
	}

	return 0;
}