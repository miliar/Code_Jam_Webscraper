#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		double C, F, X;
		cin >> C >> F >> X;

		double time = 0;
		double distance = 0;
		double speed = 2;
		while (true)
		{
			double currentTime = X / speed;
			double nextTime = C / speed + X / (speed + F);
			if (currentTime < nextTime)
			{
				time += currentTime;
				break;
			}
			time += C / speed;
			speed += F;
		}

		cout << "Case #" << nTestCase << ": " << fixed << setprecision(7) << time << endl;
	}

	return 0;
}
