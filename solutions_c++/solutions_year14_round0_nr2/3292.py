#include <cstdio>
#include <utility>
#include <algorithm>
#include <vector>
#include <set>

#define mp make_pair
#define point pair<int, int> 
#define px first
#define py second
#define INF 100000000
#define EPS 1e-9
#define rfloat(x) scanf("%lf", &(x))
#define rint(x) scanf("%d", &(x))
#define loop(i, x) for (int i = 0; i < (x); i++)


using namespace std;

double C, F, X;

bool canWin(double t)
{
	//printf("TRYING t=%lf\n", t);
	double rate = 2;
	while (true)
	{
		//printf("t=%lf, rate=%lf\n", t, rate);
		if (X / rate <= t)
			return true;
		
		if (t < 0)
			return false;
		
		t -= C / rate;
		rate += F;
	}
}

int main()
{
	int cases;
	rint(cases);
	
	loop(testcase, cases)
	{
		rfloat(C), rfloat(F), rfloat(X);
		
		double lo = 0;
		double hi = X / 2;
		while (lo < hi - 1e-10)
		{
			double mid = (lo+hi) / 2;
			if (canWin(mid))
				hi = mid;
			else
				lo = mid;
		}
		printf("Case #%d: %.7lf\n", testcase+1, lo);
	}
}