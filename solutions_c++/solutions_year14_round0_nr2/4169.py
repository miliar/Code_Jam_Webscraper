#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		double c, f, x, sol;

		scanf("%lf%lf%lf", &c, &f, &x);
		sol = x/2;

		for(int i = 1; ; i++) {
			double tot = 0;
			for(int j = 0; j < i; j++)
				tot += c/(2 + f * j);
			tot += x/(2 + f * i);
			if(tot < sol) sol = tot;
			else break;
		}

		printf("Case #%d: %.6lf\n", t, sol);
	}
}
