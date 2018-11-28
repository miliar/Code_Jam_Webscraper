/********************************************************
*      Md. Khairullah Gaurab                            *
*      Computer Science & Engineering                   *
*      Shahjalal University of Science and Technology   *
*      20th Batch                                       *
*      gaurab.cse.sust@gmail.com                        *
*********************************************************/
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

int main (int argc, char const* argv[])
{
	int test;
	double C, F, X, tres, tmpres, rate, prev;
	scanf("%d",&test);
	for (int i = 1; i <= test; i += 1)
	{
		scanf("%lf %lf %lf",&C, &F, &X);
		tres = tmpres = 0;
		rate = 2.00;
		tres += ((C/rate));
		rate += F;
		tmpres = (X/2.00);
		if(tmpres<=(tres+(X/rate))) prev = tmpres;
		else
		{
			while ((tres + (X/rate)<=tmpres))
			{
				prev = (tres + (X/rate));
				tmpres = tres + (X/rate);
				tres += (C/rate);
				rate += F;
			}
		}
		printf("Case #%d: %.8lf\n",i,prev);
	}
	return 0;
}





