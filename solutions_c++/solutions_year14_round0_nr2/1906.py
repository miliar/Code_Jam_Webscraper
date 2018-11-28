#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;

double C, F, X, ans;

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		scanf("%lf%lf%lf", &C, &F, &X);
		int k = (X*F - 2 * C) / (C*F);
		if (k <= 0) ans = X / 2;
		else {
			ans = 0;
			for (int i = 0; i < k; ++i)
				ans += C / (2 + i*F);
			ans += X / (2 + k*F);
		}
		printf("Case #%d: %.7f\n", cas, ans);
	}
	return 0;
}

