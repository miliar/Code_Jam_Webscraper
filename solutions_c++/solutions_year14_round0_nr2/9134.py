#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;
double C, F, X;
int main()
{
	int T;
	cin >> T;
	for (int cases = 1; cases <= T; cases++)
	{
		cin >> C >> F >> X;
		double speed = 2, totaltime = 0;
		double best = X / speed;
		while (true)
		{
			double t1 = C / speed;
			totaltime += t1;
			speed += F;
			if ((totaltime + X / speed) < best) {
				best = totaltime + X / speed;
			}
			else break;
		}
		printf("Case #%d: %.7lf\n", cases, best);
	}
	return 0;
}