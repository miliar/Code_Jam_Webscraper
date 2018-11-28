#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int numCases;
	const int rate = 2;
	cin >> numCases;

	for (int i=0; i<numCases; ++i)
	{
		double c, f, x;
		int n = 0; //number of farms
		cin >> c >> f >> x;

		while ((x/(rate+n*f)) > ((c/(rate+n*f)) + (x/(rate+(n+1)*f)))) n++;

		double seconds = (x/(rate+n*f));
		for (int e=0; e<n; ++e) seconds += c/(rate+e*f);

		cout << "Case #" << i+1 << ": " << setprecision(7) << fixed << seconds << endl;
	}
}