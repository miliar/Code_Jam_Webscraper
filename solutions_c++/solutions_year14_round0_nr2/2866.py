#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int ncases;
	cin >> ncases;
	
	for (int i = 1; i <= ncases; i++)
	{
		double C, F, X;
		cin >> C >> F >> X;

		double best = X;
		double elapsed = 0;
		double regen = 2.0;
		while (true)
		{
			double temp = X / regen;
			if (temp + elapsed < best)
				best = temp + elapsed;
			else
				break;
			double just_elap = C / regen;
			elapsed = elapsed + just_elap;
			regen = regen + F;
		}
		cout << std::fixed;
		cout.precision(7);
		cout << "Case #" << i << ": " << best << "\n";
	}
	return 0;
}