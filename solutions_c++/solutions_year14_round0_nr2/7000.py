#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

// R = current rate
// F = farmcookie rate
// C = farm cost
// X = win cookies
int main(int argc, char const *argv[])
{
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		double C, F, X;
		cin >> C >> F >> X;

		double time = 0.0;
		double R = 2.0;
		while (true)
		{
			double timeWin = X / R;
			double timeBuy = C / R;
			double timeBuyWin = timeBuy + X / (F + R);
			if (timeWin < timeBuyWin)
			{
				time += timeWin;
				break;
			}
			else
			{
				time += timeBuy;
				R += F;
			}
		}

		cout << "Case #" << (i+1) << ": " << setprecision(std::numeric_limits<long double>::digits10) << time << endl;
	}

	return 0;
}