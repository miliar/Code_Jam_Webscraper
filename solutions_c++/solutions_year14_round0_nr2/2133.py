#include <iostream>
#include <stdio.h>

using namespace std;

#define FOUND 1
#define BADM 2
#define CHEAT 3

int T;
double C, F, X;

int main()
{
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		const double INF = 100009;
		cin >> C >> F >> X;
		double pt = 0, ct = 0, nt = 0;
		double ptime = INF, ntime = X/2;

		double curc = 2;
		while(ptime > ntime)
		{
			ptime = ntime;
			pt = C/curc + pt;
			ntime = X/(curc + F) + pt;
			curc += F;
		}
		cout.precision(15);
		//cout << "Case #" << i << ": " << ptime << endl;
		printf ("Case #%d: %.7f\n",i , ptime);
	}
	return 0;
}
