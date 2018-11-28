#include <iostream>
#include <string>

using namespace std;

int Len(double n)
{
	int num = static_cast<int>(n), counter = 0;
	while (num != 0)
	{
		counter++;
		num /= 10;
	}
	return counter;
}


int main()
{
	int n,counter=0;
	double items[3]; // 0 - C, 1 - F, 2 - X 
	double cpr = 2.0, totalTime = 0.0, newTime = 0.0, time=0.0;

	bool finished = false;

	cout << "Enter number of tests: " << endl;
	cin >> n;

	double *times = new double [n];

	for (int index = 0; index < n; index++)
	{
		cin >> items[0] >> items[1] >> items[2];

		totalTime = 0.0;
		newTime = 0.0;
		finished = false;
		cpr = 2.0;
		counter = 0;

		time = items[2] / cpr;
		
		while (!finished)
		{
			totalTime += items[0] / cpr;
			cpr += items[1];
			newTime = (totalTime + items[2] / cpr);
			if (time >= newTime)
			{
				time = newTime;
				counter = 0;
			}

			if (counter >= 50)
				finished = true;

			counter++;
		}

		times[index] = time;
	}

	

	for (int i = 0; i < n; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		cout.precision(Len(times[i]) + 7);
		cout << times[i] << endl;
	}
	cin.ignore(2);
	return 0;
}