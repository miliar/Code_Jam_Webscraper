#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#define eps 1e-7

using namespace std;

int main()
{
	freopen("1.txt", "r", stdin);	
	freopen("2.txt", "w", stdout);	
	int cas, T;
	
	for (cas=scanf("%d", &T); cas<=T; cas++)
	{
		double C, F, X;
		cin >> C >> F >> X;
		
		double v = 2, ans = X / 2, t = 0;
		while (X * F >= v * C - eps)
		{
			ans = min(ans, t + X / v);
			t += C / v;
			v += F;
		}
		printf("Case #%d: %.7f\n", cas, ans);
	}
    return 0;
}
