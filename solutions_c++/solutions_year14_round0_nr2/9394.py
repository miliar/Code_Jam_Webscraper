#include <iostream>
#include <fstream>
using namespace std;

double fastestWin(double, double, double, double, double);

int main()
{
	int T;
	cin >> T;
	ofstream out("output.out");
	out.precision(14);
	for (int i = 0; i < T; i++)
	{
		double C, F, X;
		cin >> C >> F >> X;
		double rate = 2;
		double time = fastestWin(C, F, X, rate, 0);
		out << "Case #" << i + 1 << ": " << time;
		if (i != T - 1)
			out << "\n";
	}
	out.close();
	return 0;
}

double fastestWin(double C, double F, double X, double rate, double currTime)
{
	double time1 = C / rate + X / (rate + F);
	double time2 = X / rate;
	if (time1 < time2)
		return fastestWin(C, F, X, rate + F, currTime + C / rate);
	else return currTime + time2;
}