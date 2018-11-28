#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <cassert>
#include <climits>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
#define mp make_pair
#define sqr(x) ((x)*(x))
const double PI = 3.1415926535;

long long a;
int d[1005000], n, t, cur, ans;

int main()
{
#ifdef MYLOCAL
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

	scanf("%d", &t);
	for (int _ = 1; _ <= t; ++_)
	{
		printf("Case #%d: ", _);
		scanf("%d %d", &a, &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", &d[i]);
		sort(d, d+n);
		cur = 0, ans = INT_MAX;
		if (a == 1)
		{
			printf("%d\n", n);
			continue;
		}
		for (int i = 0; i < n; ++i)
		{
			if (a > d[i])
				a += d[i];
			else
			{
				ans = min(ans, cur + (n - i));
				while (a <= d[i])
					a = 2 * a - 1, ++cur;
				a += d[i];
			}
		}
		ans = min(ans, cur);
		printf("%d\n", ans);
	}
    
    return 0;
}