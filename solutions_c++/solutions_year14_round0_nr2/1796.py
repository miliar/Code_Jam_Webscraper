#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;
const long long MOD = 1000000007;

int set[100];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	scanf("%d", &T);
	
	for (int nt = 1; nt <= T; ++nt)
	{
		double C, F, X;
		scanf("%lf%lf%lf", &C, &F, &X);
		double v = 2;
		double ans = 0;
		for (v = 2; v*C < (X-C)*F; v += F)
			ans += C/v;
		ans += X/v;
		printf("Case #%d: %.7f\n", nt, ans);
	}
	return 0;
}