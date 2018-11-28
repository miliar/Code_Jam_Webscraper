#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int Count; scanf("%d",&Count);
	for(int T = 1; T <= Count; ++T)
	{
		double C, F, X;
		scanf("%lf%lf%lf", &C, &F, &X);

		double rate = 2;
		double ans = X / rate;
		double cur = 0;

		while(1)
		{
			cur += C / rate;
			if(cur > ans)
				break;
			rate += F;
			double tmp = cur + X / rate;
			if(tmp < ans)
				ans = tmp;
		}

		printf("Case #%d: %.8lf\n", T, ans);
	}
}
