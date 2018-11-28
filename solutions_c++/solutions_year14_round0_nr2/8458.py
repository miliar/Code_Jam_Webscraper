#include <iostream>
#include <iomanip>
#include <limits>
using namespace std;

void solveA(int t)
{
	double c,f,x;
	cin >> c >> f >> x;

	bool stop = false;
	double minTime = numeric_limits<double>::max();
	int n = 0;
	do
	{
		double time = 0;
		time += x / ( 2 + n*f );
		//cout << "x / ( 2 + n*f ) - " << time << endl;

		for (int i = 0; i < n; i++)
		{
			time += c / ( 2 + i*f );
			//cout << "time += c / ( 2 + i*f ); - " << c / ( 2 + i*f ) << endl;
		}

		if (minTime > time)
			minTime = time;
		else
			stop = true;
		n += 1;
		//cout << "stop" << stop << endl;
	} while (!stop);

	cout << fixed << setprecision(7) << "Case #" << t << ": " << minTime;
	
	cout << endl;
}

void a()
{
	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		solveA(i+1);
	}
}

int main()
{
	a();
	return 0;
}