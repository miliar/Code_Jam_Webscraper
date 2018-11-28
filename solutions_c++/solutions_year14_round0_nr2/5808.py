#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		double c, f, x;
		cin >> c >> f >> x;
		
		double best = x / 2;
		for (double j = 1; true; j++)
		{
			double next = 0;
			for (double k = 0; k < j; k++)
			{
				next += c / (2 + k*f);
			}
			next += x / (2 + j*f);
			
			if (next < best)
				best = next;
			else
				break;
		}
		cout << "Case #" << i << ": " << setprecision(7) << fixed << best << endl;
	}
	return 0;
}