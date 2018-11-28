#include <iostream>
using namespace std;
void main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	double C, F, X;
	double sum, m, n;
	double f;
	int T, t;
	cin >> T;

	for (t = 1; t <= T; t++)
	{

		cin >> C >> F >> X;

		f = 2;
		m = C / f;
		n = X / (F + f);
		sum = 0;
		while (X / f > n + m)
		{
			sum += C / f;
			f += F;
			m = C / f;
			n = X / (F + f);
		}
		sum += X / f;

		cout.setf(ios::fixed);
		cout.precision(7);
		cout << "Case #" << t << ':';
		cout << ' ' <<sum << endl;
	}
}