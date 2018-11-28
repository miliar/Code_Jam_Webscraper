#include <cstdio>
#include <queue>
#include <cassert>
#include <cstring>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
using namespace std;

typedef long long ll;

#define eps 1e-7

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);
		double curTime = 0.0;
		double curGain = 2.0; 
		double res = 1e10;
		while(res - (curTime + x / curGain) > eps)
		{
			res = curTime + x / curGain;
			curTime += c / curGain;
			curGain += f;
		}
		printf("Case #%d: %.7lf\n", t, res);
	}
	return 0;
}