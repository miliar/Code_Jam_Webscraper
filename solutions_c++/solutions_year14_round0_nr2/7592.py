#include <cstdio>
using namespace std;

int main()
{
	int t;
	scanf ("%d", &t);
	for (int j = 0; j < t; j++) {
		double c, f, x;
		scanf ("%lf %lf %lf", &c, &f, &x);
		double time = 100000000;
		int k = 0;
		while (1) {
			double ntime = 0;
			for (int i = 0; i < k; i++)
				ntime += c / (2 + i * f);
			ntime += x / (2 + k * f);
			if (ntime > time) break;
			time = ntime;
			k++;
		}
		printf ("Case #%d: %.7f\n", j+1, time);
	}
	return 0;
}
