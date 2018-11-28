#include <fstream>
#include <cstdio>
using namespace std;
int T;
double C, F, X, sol, now, rate;

int main()
{
	int t;
	ifstream fin("B.in");
	freopen("B.out", "w", stdout);
	fin >> T;
	for(t = 1; t <= T; ++t)
	{
		fin >> C >> F >> X;
		now = 0.0;
		rate = 2.0;
		sol = X / rate;
		while(1)
		{
			now += (C / rate);
			rate += F;
			if(sol > now + (X / rate))
				sol = now + (X / rate);
			else
				break;
		}
		printf("Case #%d: %.7lf\n", t, sol);
	}
	fin.close();
	return 0;
}
