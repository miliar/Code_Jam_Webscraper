#include <iostream>

using namespace std;

int main()
{
	int numCases;
	cin >> numCases;
	bool done;
	for (int i = 1; i <= numCases; ++i)
	{
		double C, F, X, f = 2.00000, buy, nobuy, total = 0.00000;
		cin >> C;
		cin >> F;
		cin >> X;
		done = false;
		while(!done)
		{
			buy = C / f + X / (F + f);
			nobuy = X / f;
			if(buy < nobuy)
			{
				total += C / f;
				f += F;
			}
			else
			{
				total += nobuy;
				cout << "Case #" << i << ": ";
				cout.precision(7);
				cout << fixed;
				cout << total << endl;
				done = true;
			}
		}
	}
}