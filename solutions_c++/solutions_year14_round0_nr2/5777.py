#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

int main()
{
	int t;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);
		double cps = 2;
		double prev = x / cps;
		double sum = 0;
		while (1)
		{
			sum += c / cps;
			cps += f;
			double cur = sum + x / cps;
			if (prev < cur)
				break;
			prev = cur;
		}
		printf("Case #%d: ", i);
		printf("%lf", prev);
		printf("\n");
	}
	return 0;
}