#include <iostream>

using namespace std;

void doit(int casenum)
{
	cout << "Case #" << casenum << ": ";

	double C, F, X;
	cin >> C >> F >> X;	

	double best = INFINITY;
	double time = 0;
	for (int farms = 0;; ++farms)
	{
		double rate = 2.0 + farms * F;
		double cur = time + X / rate;
		if (cur >= best) break;
		best = cur;
		time += C / rate;
	}
	cout << best << endl;
}

int main()
{
	cout.precision(7);
	cout.setf(ios::fixed);

	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) doit(i);
	return 0;
}