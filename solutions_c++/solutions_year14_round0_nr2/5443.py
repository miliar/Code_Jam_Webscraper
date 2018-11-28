#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <vector>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int z = 1; z <= T; ++z)
	{
		printf("Case #%d: ", z);
		long double c, f, x;
		scanf("%Lf %Lf %Lf", &c, &f, &x);
		long double v = 2.0l;
		long double t = x / v;
		long double curExtraT = 0.0l;
		while (curExtraT < t)
		{
			curExtraT += (c / v);
			v += f;
			t = min(t, curExtraT + (x / v));
		}
		printf("%.9Lf\n", t);
	}
	return 0;
}