// #include "include\preCompile\KL_PreCompile.hpp"
#include "KL_PreCompile.hpp"

void init()
{
}

int main()
{
	clock_t time1;
	time1 = clock();

	int counter = 0;
	// while (counter++ < 10000)
	{
		freopen("D:\\DUMP\\input.in", "r", stdin);
		freopen("D:\\DUMP\\output.out", "w", stdout);

		int T;
		cin >> T;
		// double CMax = 10000., FMax = 100., XMax = 100000.;


		for (long long int caseNum = 1; caseNum <= T; caseNum++)
		{
			double C, X, F;
			double currentTotal = 0;
			double currentRate = 2.0;
			double timeTaken = 0.;
			cin >> C >> F >> X;

#if 0
			C = fabs( (double)rand()/RAND_MAX) * (CMax - 9000.) + 9000.;
			F = fabs( (double)rand()/RAND_MAX ) * (FMax - 90.) + 90.;
			X = fabs( ( (double)rand() ) /(double)RAND_MAX ) * (XMax - 90000.) + 90000.;
#endif


			double tmp4 = 0.;
			double tmp2 = 0.;

			while (1)
			{
				double tmp1 = (X*F) / (F + currentRate);
				//double tmp3 = X/(F+currentRate);

				if ( X <= C || ( 0 < (C - tmp1) ) )
				{
					tmp4 = X/currentRate;
					timeTaken += tmp4;

					break;
				}
				else
				{
					tmp2 = C/currentRate;
					timeTaken += tmp2;
					currentRate += F;
				}
			}


			cout << "Case #" << caseNum << ": " << fixed << setprecision(7) << timeTaken << endl;
		}

		fclose(stdin);
		fclose(stdout);

	}
#if 0
	clock_t time2, timeTaken;
	time2 = clock();
	timeTaken = time2 - time1;
	long long int seconds = timeTaken/CLOCKS_PER_SEC;
	long long int minutes = seconds/60;
	seconds %= 60;
	cout << minutes << "min" << seconds << "sec";
#endif
}
