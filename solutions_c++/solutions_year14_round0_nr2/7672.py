#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

void solve()
{
	double C, F, X,ans;
	int n,i;

	scanf("%lf%lf%lf", &C, &F, &X);
	n = int(X / C - 2 / F);
	if (n < 0)
		n = 0;

	ans = X / (n*F + 2);
	for (i = n - 1; i >= 0; i--)
		ans += C / (i*F + 2);
	printf("%.7lf\n", ans);
}

int main()
{
	int T;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}