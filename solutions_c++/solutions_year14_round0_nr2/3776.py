#include <iostream>

using namespace std;

#define REP(v, repeat) for(int v=0; v<(repeat); ++v)
#define REPD(v, repeat) for(int v=(repeat)-1; v>=0; --v)
#define FOR(v, start, end) for(int v=(start); v<=(end); ++v)
#define FORD(v, start, end) for(int v=(start); v>=(end); --v)
#define ROUNDING(x, dig) (floor((x) * pow(10, dig) + 0.5f) / pow(10, dig))
#define INF 99999999

int main()
{
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w+", stdout);
#endif

	int t;
	scanf("%d", &t);
	FOR(tc, 1, t)
	{
		double c, f, x, tick = 2, sec = 0;
		scanf("%lf%lf%lf", &c, &f, &x);
		double minn = x / tick;
		double ret = 0;

		while (1)
		{
			sec += (c / tick);
			tick += f;
			ret = (sec + x / tick);
			if (ret < minn) minn = ret;
			else break;
		}
		printf("Case #%d: %.7f\n", tc, minn);
	}
	return 0;
}