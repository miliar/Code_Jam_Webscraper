#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <cmath>
#define MAXN 105
#define MYINF 1000000000

using namespace std;

int main ()
{
	int T, iT;
	scanf("%d",&T);
	static double R[MAXN];
	static double C[MAXN];
	for (iT = 0; iT < T; iT++)
	{
		int N;
		double V, X;
		scanf("%d %lf %lf",&N,&V,&X);
		int i;
		for (i = 0; i < N; i++)
		{
			scanf("%lf %lf",&(R[i]),&(C[i]));
		}
		char possible = 0;
		double res = 0.0;

		for (i = 0; i < N; i++)
		{
			if (fabs(C[i] - X) <= 1E-9)
			{
				double temp = V / R[i];
				if (!possible) { res = temp; possible = 1; }
				else if (temp < res) res = temp;
			}
		}

		int j;
		for (i = 0; i < N; i++)
		{
			for (j = i+1; j < N; j++)
			{
				if (fabs(C[i] - C[j]) <= 1E-9)
				{
					if (fabs(C[i] - X) <= 1E-9)
					{
						double temp = V / (R[i] + R[j]);
						if (!possible) { res = temp; possible = 1; }
						else if (temp < res) res = temp;
					}
				}
				else
				{
					double xi = ((X - C[j]) * V) / (C[i] - C[j]);
					double xj = V - xi;
					if ((xi >= 0.0) && (xi <= V))
					{
						double temp = xi / R[i];
						if ((xj / R[j]) > temp) temp = xj / R[j];
						if (!possible) { res = temp; possible = 1; }
						else if (temp < res) res = temp;
					}
				}
			}
		}

		printf("Case #%d: ",iT+1);
		if (possible == 0) printf("IMPOSSIBLE\n");
		else printf("%.9lf\n",res);
	}
	return 0;
}
