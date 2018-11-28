#pragma comment(linker, "/STACK:256000000")

#include <iostream>
#include <iomanip>

#include <map>
#include <set>
#include <vector>
#include <string>

#include <queue>
#include <deque>
#include <stack>

#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cstdarg>
#include <algorithm>

#include <complex>

#include <sstream>

using namespace std;

#define sqr(x) ((x)*(x))

int a[1007];

int main()
{
	#ifdef CRABEN
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#else
	#endif

	int t; scanf("%d\n", &t);
	for (int num = 1; num <= t; num++)
	{
		int d; scanf("%d", &d);

		memset(a, 0, sizeof(a));
		for (int i = 0; i < d; i++)
		{
			int v; scanf("%d", &v);
			a[v]++; 
		}

		int ans = 10007;
		for (int i = 1; i <= 1000; i++)
		{
			int count = 0;
			for (int j = i + 1; j <= 1000; j++)
				count += ((j + i - 1) / i - 1) * a[j];
			ans = min(ans, count + i);
		}

		printf("Case #%d: %d\n", num, ans);
	}

	return 0;
}