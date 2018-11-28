#include <iostream>
using namespace std;

double C,F,X;
void solve(int tc)
{	
	scanf("%lf %lf %lf", &C, &F, &X);
	double ans = X / 2.0;
	double t = 0.0;	//use time
	double v = 2.0;
	while (t < ans)
	{
		t += C / v;
		v += F;
		if (X / v + t - ans < 0)
		{
			ans = X / v + t;
		}
	}
	printf("Case #%d: %.7lf\n", tc, ans);
}
int main()
{
//	freopen("c:\\data\\B-large.in", "r", stdin);
//	freopen("c:\\data\\B-large.out", "w", stdout);
	
	int tc;
	scanf("%d", &tc);
	int i;
	for (i = 1; i <= tc; i++)
	{
		solve(i);
	}
	return 0;
}