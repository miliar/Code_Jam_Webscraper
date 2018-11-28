#include <cstdio>
using namespace std;
long double c, f, x,myc, myf, myx, res;
int t, n;

long double solve()
{
	long double tt, res = 0;
	if(c >= x)
	{
		//printf("%.7llf\n", x/myf);
	}

	myx = c;

	while(true)
	{
		tt = c / myf;
		res += tt;
		if((x-myx)/myf > c/f)
			myf += f;
		else
			break;
	}
	res += (x-myx) / myf;
	return res;
}

int main()
{
	scanf("%d", &n);
	t = 0;
	while(t++ < n)
	{
		myc = myx = 0.0;
		myf = 2.0;
		scanf("%llf%llf%llf", &c, &f, &x);
		printf("Case #%d: %.7llf\n", t, solve());
	}
}