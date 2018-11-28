#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

#define For(i, a, b) for(int i=a; i<b; ++i)
#define MP make_pair
#define INF (1<<30)

using namespace std;

typedef pair <int, int> ii;

int main()
{
	int T;
	scanf("%d", &T);

	For(caso, 1, T+1)
	{
		double C, F, X;
		scanf("%lf %lf %lf", &C, &F, &X);

		double sec = 0.0, act = 0.0, rate = 2.0;

		while (true)
		{
			//cout << act << endl;

			double tC = C/rate, tX = (X - act)/rate;

			if (tX < tC)
			{
				sec += tX;
				break;
			}

			sec += tC;
			act += C;

			double nR = rate + F;
			if ((X-act)/rate > X/nR)
			{
				act  = 0.0;
				rate = nR;
			}
		}

		printf("Case #%d: %.7lf\n", caso, sec);

	}

	return 0;
}