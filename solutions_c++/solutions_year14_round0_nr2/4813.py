#include <iostream>

using namespace std;

double best_time(double c, double f, double x);

int main()
{
	int T;
	cin >> T;

	for (int test = 1; test <= T; test++)
	{
		double c, f, x;
		cin >> c >> f >> x;

		cout << "Case #" << test << ": ";
		cout.precision(7);
		cout << fixed << best_time(c, f, x) << endl;
	}

	return 0;
}

double time_to_win(int farms, double c, double f, double x)
{
	double total = 0;

	for (int i = 0; i < farms; i++)
	{
		total += c/(2.0 + f*i);
	}

	total += x/(2.0 + farms*f);

	return total;
}

double 
best_time(double c, double f, double x)
{
	int n = 0;

	double prev = time_to_win(n, c, f, x);	
	n++;

	double next = time_to_win(n, c, f, x);	
	n++;
	
	while (next < prev)
	{
		prev = next;
		next = time_to_win(n, c, f, x);
		n++;
	}

	return prev;
}

