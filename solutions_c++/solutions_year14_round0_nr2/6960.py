#include "cstdio"
int T;
void work()
{
	double C, F, X;
	scanf("%lf%lf%lf", &C, &F, &X);
	double now = 2., tim = 0.;
	for (;;) {
		if (X / now >= C / now + X / (now + F))
		{
			tim += C / now;
			now += F;
//			printf("%lf %lf\n", tim, now);
		} else {
			break;
		}
	}
	tim += X / now;
	printf("%.7lf\n", tim);
}
int main(int argc, char const *argv[])
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf("Case #%d: ", i + 1);
		work();
	}
	return 0;
}