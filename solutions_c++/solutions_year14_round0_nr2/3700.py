#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int T;
	long double value, C, F, X, cookiesPerSecond;

	cin >> T;
	for(int val=1; val <= T; val++)
	{
		value = 0.0;
		cookiesPerSecond = 2.0;
		cin >> C >> F >> X;

		while(C/cookiesPerSecond + X/(cookiesPerSecond + F) < X/(cookiesPerSecond))
		{
			value += C/cookiesPerSecond;
			cookiesPerSecond += F;
		}

		value += X/(cookiesPerSecond);

		cout << fixed << setprecision(7) << "Case #" << val << ": " << value << endl;
	}
	return 0;
}