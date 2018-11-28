#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
	ofstream fout("testout.out", ios::out);
	ifstream fin("testin.in");

	int tests; fin >> tests;

	for (int i = 0; i < tests; i++)
	{
		double C, F, X; fin >> C >> F >> X;
		double time = 0.0, rate = 2.0;
		double answer;

		while (time != X)
		{
			if (time + X / rate <= time + C / (rate) + X / (F + rate))
			{
				answer = time + X / rate;
				time = X;
			}
			else
			{
				time = time + C / (rate);
				rate += F;
			}
		}
		fout << "Case #" << i + 1 << ": " << fixed << setprecision(7) << answer << endl;
	}

	return 0;
}