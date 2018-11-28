#include <stdio.h>

double min(double x, double y)
{
	return x<y?x:y;
}

double C, F, X;
//C: cookies per farm
//F: cookies per sec
//X: target cookies
double letsBakeSomeCookies (double f, double t)
{
	if (X/f<=(C/f+X/(f+F))) return t+X/f;
	return min (t+X/f, letsBakeSomeCookies(f+F, t+C/f));
}

int main(int argc, char const *argv[])
{
	freopen (argv[1], "r", stdin);
	freopen (argv[2], "w", stdout);
	int T;
	scanf ("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf ("%lf %lf %lf", &C, &F, &X);
		printf("Case #%d: %.7lf\n", t, letsBakeSomeCookies(2, 0));
	}
	return 0;
}