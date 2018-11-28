#include <cstdio>
typedef double DB; 

double a[100001], S[100001], res[100001];

const double Epsilon = 1e-7;

int main()
{
	int t;
    double C, F, X;

	scanf ("%d", &t);

	for (int test = 1; test <= t; test++)
	{
    	scanf ("%lf%lf%lf", &C, &F, &X);

		S[0] = a[0] = 0;

		res[0] = X * 0.5;

		for (int i=1; i<=100000; i++)
		{
		    a[i] = C / (2.0 + F * ((DB)(i - 1)));
		    S[i] = S[i - 1] + a[i];
		    res[i] = S[i] + X / (F * ((DB)i) + 2.0);

			if (res[i] - res[i- 1] > -Epsilon)
			{
				printf("Case #%d: %.7lf\n", test, res[i - 1]);
				break;
			}
		}
	}

	return 0;
}
