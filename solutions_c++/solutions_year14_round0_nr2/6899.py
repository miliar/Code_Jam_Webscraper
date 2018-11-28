#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for(int t = 0; t < T; t++)
	{
		double C, F, X;
		cin >> C;
		cin >> F;
		cin >> X;

		double currentRate = 2.0;
		double currentTime = 0.0;

		while(true)
		{
			if(X/currentRate < (X/(currentRate+F) + C/currentRate))
			{
				currentTime += X/currentRate;
				break;
			}
			else
			{
				currentTime += C/currentRate;
				currentRate += F;
			}
		}

		cout << fixed;
		cout << "Case #" << (t+1) << ": " << setprecision(7) << currentTime << endl;
	}
}
