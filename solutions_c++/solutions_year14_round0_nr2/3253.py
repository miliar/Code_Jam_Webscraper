#include <iostream>

using namespace std;

double calculateTime(double C, double F, double X, double T)
{
	double timeWithoutBuilding = X / T;
	double timeToBuild = C / T;
	double timeWithBuilding = timeToBuild + (X / (T + F));

	if (timeWithoutBuilding <= timeWithBuilding)
	{
		return timeWithoutBuilding;
	}

	return timeToBuild + calculateTime(C, F, X, T + F);
}

int main(int argc, char *argv[])
{
	unsigned nrTCs;
	cin >> nrTCs;
	for(unsigned i = 0; i < nrTCs; i++)
	{
		double C, F, X;
		cin >> C >> F >> X;

		double t = calculateTime(C, F, X, 2.0);

		cout.precision(7);
		cout << "Case #" << (i + 1) <<": " << fixed <<  t << "\n";
	}

	return 0;
}