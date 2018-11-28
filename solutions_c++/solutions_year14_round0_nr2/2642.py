#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
double c, f, x;

inline double calc(int k)
{
	double sum=x/(k*f+2.0);
	for (int i=0; i<k; ++i) sum+=c/(i*f+2.0);
	return sum;
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T, k;
	double time;
	scanf("%d", &T);
	for (int tt=1; tt<=T; ++tt)
	{
		scanf("%lf%lf%lf", &c, &f, &x);
		k=max((int)ceil(x/c-2.0/f-1.0), 0);
		time=min(calc(k), calc(k+1));
		if (k) time=min(time, calc(k-1));
		printf("Case #%d: %.7f\n", tt, time);
	}
	return 0;
}

