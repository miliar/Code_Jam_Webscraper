#include<cstdio>
#include<cmath>

using namespace std;

int main()
{
	int P, Q, iT, ancestor, T ;
	long double Result;
	long long mulTimes,  iResult, div;
	bool isPossible;
	freopen("Problem A. Part Elf.in", "r", stdin);
	freopen("Problem A. Part Elf.out", "w", stdout);
	scanf("%d", &T);
	for (iT = 1; iT <= T; iT++)
	{
		scanf("%d/%d", &P, &Q);
		isPossible = false;
		Result = (long double)P/(long double) Q *powl(2.0,41.0);
		iResult = floor(Result);
		div = powl(2.0, 41.0);
		printf("Case #%d: ", iT);
		if (floor(Result) == Result)
		{
			for (mulTimes = 0; mulTimes <= 41; mulTimes++)
			{
				if( iResult/div )
				{
					ancestor = mulTimes ;
					isPossible = true;
					break;
				}
				
				div /= 2;

			}
		}
		if (isPossible)
			printf("%d\n", ancestor);
		else
		{

			printf("impossible\n");
		}

	}
}