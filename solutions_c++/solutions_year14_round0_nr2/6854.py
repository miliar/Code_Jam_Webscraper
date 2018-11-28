#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t)
	{
		double C, F, X;
		cin >> C >> F >> X;

		double prev = X/2.0, next = X/2.0, timeSpent = 0, i = 0.0, rate = 2.0;
		
		while(next <= prev)
		{
			prev = next;
			timeSpent += (C/rate);
			rate += F;
			next = timeSpent + X/rate;
		}

		cout << "Case #" << t << ": " << setprecision(7) << fixed << prev << "\n";
	}
	return 0;
}