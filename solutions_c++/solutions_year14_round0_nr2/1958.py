#include <stdio.h>
#define REP(i, n) for (i = 0; i < (n); i++)
#define REP1(i, n) for (i = 1; i <= (n); i++)
using namespace std;

int nowtd, tdnum;

double ans, c, f, x;

void ri()
{
	ans = 0;
	scanf("%lf%lf%lf", &c, &f, &x);
}

void solve()
{
	double delta;

	int i;
	
	ans = x / 2;
	REP(i, 1000000)
	{
		delta = (c - x) / (2 + i * f) + x / (2 + (i + 1) * f);
		if (delta < 1e-11) ans += delta; else break;
	}
}

void print() {printf("Case #%d: %.7f\n", nowtd, ans);}

int main()
{
	scanf("%d", &tdnum);
	REP1(nowtd, tdnum)
	{
		ri();
		solve();
		print();
	}
	return 0;
}
