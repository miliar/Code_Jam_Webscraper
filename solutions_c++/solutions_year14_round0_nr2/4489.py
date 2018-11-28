#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <string>

using namespace std;

double calc(double C, double F, double X)
{
	double result = INT_MAX;
	double rate = 2;
	double time = 0;
	while (true)
	{
		double cur = X / rate + time;
		if (cur >= result)
			break;
		result = cur;
		time += C / rate;
		rate += F;
	}
	return result;
}

int main()
{
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	int T;
	in >> T;
	double C, F, X;
	for (int k = 0; k < T; k++)
	{
		in >> C >> F >> X;
		double result = calc(C, F, X);
		out << setiosflags(ios::fixed) << setprecision(7) << "Case #" << k + 1 << ": " << result << endl;
	}
	out.close();
	system("PAUSE");
	return 0;
}